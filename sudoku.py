import math


class SudokuManager:
    def __init__(self, flat_array):
        self._arr = flat_array

    def __deepcopy__(self, memo={}):
        return SudokuManager(self._arr[:])

    def find_an_empty_cell(self):
        try:
            i = self._arr.index(0)
            return (i // 9, i % 9)
        except ValueError:
            return None

    def get_allowed_vals(self, row, col):
        used_vals = set()
        for i in range(9):
            used_vals.add(self._arr[9*row + i])  # Cells in the same row
            used_vals.add(self._arr[9*i + col])  # Cells in the same column

        row = (row // 3) * 3
        col = (col // 3) * 3
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                used_vals.add(self._arr[9*i + j])

        allowed_vals = set(range(1, 10)).difference(used_vals)
        return allowed_vals

    def mark(self, row, col, val):
        self._arr[9 * row + col] = val

    def to_matrix(self):
        return [self._arr[9*i:9*(i+1)] for i in range(9)]
