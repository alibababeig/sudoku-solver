import argparse
import time

from engine.sudoku import solve
from engine.sudoku import SudokuManager
from utils.cli import CliManager
from utils.input import InputManager


def main():
    waiting_time = 1  # seconds

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input", required=True,
        help='Path to the file containing the Sudoku puzzle layout')
    args = parser.parse_args()

    c = CliManager()
    i = InputManager()
    try:
        m = i.load(args.input)
    except FileNotFoundError:
        c.print_txt(f'Could not find the input file at "{args.input}".')
        exit(1)
    except ValueError:
        c.print_txt(f'The provided input file does not have a valid format.')
        exit(1)

    puzzle = SudokuManager(m)
    if not puzzle.is_valid():
        c.print_txt(f'The provided Sudoku puzzle is not valid.')
        exit(1)

    c.clear()
    c.print_txt('\n               Puzzle')
    c.print_sudoku(puzzle.to_matrix(), end='\n\n')
    c.print_txt(f'Solving...')

    tik = time.time()
    solution = solve(puzzle)
    tok = time.time()
    exec_time = tok - tik

    if exec_time < waiting_time:
        time.sleep(waiting_time - exec_time)

    if solution == None:
        c.print_txt('Could not find a solution. '
                    'Are you sure that the puzzle is solvable?')
    else:
        c.clear()
        c.print_txt('\n               Puzzle                \t\t'
                    '              Solution')
        c.print_sudoku_side_by_side(
            puzzle.to_matrix(), solution.to_matrix(), delim='\t\t', end='\n\n')

    c.print_txt(f'Processing Time = {exec_time:,.3f} s')


if __name__ == '__main__':
    main()
