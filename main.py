import copy
import time

from sudoku import SudokuManager
from utils.cli import CliManager
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
    waiting_time = 0.5  # seconds

    c = CliManager()
    i = InputManager()
    m = i.load(f'input4.txt')
    puzzle = SudokuManager(m)

    c.clear()
    c.print_sudoku(puzzle.to_matrix(), end='\n\n')
    c.print_txt(f'Solving...')

    tik = time.time()
    solution = solve(puzzle)
    tok = time.time()
    exec_time = tok - tik

    if exec_time < waiting_time:
        time.sleep(waiting_time - exec_time)

    c.clear()
    c.print_sudoku_side_by_side(
        puzzle.to_matrix(), solution.to_matrix(), end='\n\n')

    c.print_txt(f'Processing Time = {exec_time:,.3f} s')


if __name__ == '__main__':
    main()
