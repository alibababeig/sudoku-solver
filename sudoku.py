import math


class SudokuManager:
    def __init__(self, matrix):
        self._matrix = matrix

    def __deepcopy__(self, memo={}):
        m = [x[:] for x in self._matrix]
        return SudokuManager(m)

    def find_an_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self._matrix[i][j] == 0:
                    return (i, j)
        return None

    def get_allowed_vals(self, row, col):
        used_vals = set()
        for i in range(9):
            used_vals.add(self._matrix[row][i])  # Cells in the same row
            used_vals.add(self._matrix[i][col])  # Cells in the same column

        row = (row // 3) * 3
        col = (col // 3) * 3
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                used_vals.add(self._matrix[i][j])

        allowed_vals = set(range(1, 10)).difference(used_vals)
        return allowed_vals

    def mark(self, row, col, val):
        self._matrix[row][col] = val

    def to_matrix(self):
        return self._matrix
