import os
import subprocess


class CliManager:
    def __init__(self):
        self._clear_cmd = 'cls' if os.name == 'nt' else 'clear'

    def clear(self):
        subprocess.call(self._clear_cmd)

    def print_sudoku(self, matrix, end='\n'):
        matrix_str = self._generate_sudoku_str(matrix)
        print(matrix_str, end=end)

    def print_sudoku_side_by_side(self, a, b, delim='\t', end='\n'):
        a_str = self._generate_sudoku_str(a)
        b_str = self._generate_sudoku_str(b)

        a_list = a_str.split('\n')
        b_list = b_str.split('\n')

        final_str = '\n'.join(
            [f'{x}{delim}{y}' for x, y in zip(a_list, b_list)])
        print(final_str, end=end)

    def print_txt(self, txt, end='\n'):
        print(txt, end=end)

    def _generate_sudoku_str(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # Replace zero values with whitespaces for a
        # visually better representation of the sudoku table
        for i in range(m):
            matrix[i] = [' ' if x == 0 else x for x in matrix[i]]

        matrix_str = '┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓\n'
        for i, row in enumerate(matrix):
            matrix_str += self._generate_sudoku_row_str(row) + '\n'

            if i == m - 1:  # End of the Sudoku table
                s = '┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛'
            else:
                if i % 3 == 2:  # Bold horizontal line
                    s = '┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫\n'
                else:  # Regular horizontal line
                    s = '┠───┼───┼───╂───┼───┼───╂───┼───┼───┨\n'

            matrix_str += s

        return matrix_str

    def _generate_sudoku_row_str(self, row):
        row_str = '┃' + '│'.join([f' {x} ' for x in row]) + '┃'
        return row_str[:12] + '┃' + row_str[13:24] + '┃' + row_str[25:]
