import copy
import time

from sudoku import SudokuManager
from utils.input import InputManager


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


def main():
    i = InputManager()

    for j in range(1, 7):
        m = i.load(f'input{j}.txt')
        s = SudokuManager(m)

        tik = time.time()
        s = solve(s)
        tok = time.time()

        print(f'Sudoku #{j} Calculation Time = {(tok - tik) * 1000:8,.1f} ms')

    # for r in s.to_matrix():
    #     print('\t'.join(map(str, r)))


if __name__ == '__main__':
    main()
