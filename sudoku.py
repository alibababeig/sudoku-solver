import math


class SudokuManager:
    def __init__(self, matrix):
        if len(matrix) != 9:
            raise ValueError()

        for row in matrix:
            if len(row) != 9:
                raise ValueError()
            for x in row:
                if x not in range(10):
                    raise ValueError()

        self._matrix = matrix

    def find_an_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self._matrix[i][j] == 0:
                    return (i, j)
        return None

    def get_allowed_vals(self, row, col):
        if self._matrix[row][col] > 0:
            return {self._matrix[row][col]}

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
        if self._matrix[row][col] > 0:
            raise ValueError()
        if val not in self.get_allowed_vals(row, col):
            raise ValueError()
        self._matrix[row][col] = val

    def to_matrix(self):
        return self._matrix
