import copy


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

    def is_valid(self):
        return self._is_valid_row() and \
            self._is_valid_column() and self._is_valid_square()

    def mark(self, row, col, val):
        self._arr[9 * row + col] = val

    def to_matrix(self):
        return [self._arr[9*i:9*(i+1)] for i in range(9)]

    def _is_valid_row(self):
        for i in range(9):  # Iterate on Sudoku rows
            s = set()  # Maintain a set of values in each row
            for j in range(9):
                x = self._arr[9*i + j]
                if x > 0 and x in s:  # Duplicate number in a Sudoku row!
                    return False
                s.add(x)
        return True

    def _is_valid_column(self):
        for i in range(9):  # Iterate on Sudoku columns
            s = set()  # Maintain a set of values in each column
            for j in range(9):
                x = self._arr[9*j + i]
                if x > 0 and x in s:  # Duplicate number in a Sudoku column!
                    return False
                s.add(x)
        return True

    def _is_valid_square(self):
        for i in range(9):  # Iterate on Sudoku squares
            s = set()  # Maintain a set of values in each square
            row = (i // 3) * 3
            col = (i % 3) * 3
            for j in range(row, row + 3):
                for k in range(col, col + 3):
                    x = self._arr[9*j + k]
                    if x > 0 and x in s:  # Duplicate number in a Sudoku square!
                        return False
                    s.add(x)
        return True


def solve(sudoku):
    coordination = sudoku.find_an_empty_cell()
    if coordination == None:
        return sudoku

    row, col = coordination
    for val in sudoku.get_allowed_vals(row, col):
        s = copy.deepcopy(sudoku)
        s.mark(row, col, val)
        s = solve(s)
        if s != None:
            return s

    return None
