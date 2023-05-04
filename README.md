<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple Sudoku solver written in Python as a side project and purely out of boredom!

The Sudoku solver utilizes a backtracking approach to find the correct values for each cell of the Sudoku table. Since the solver is written entirely in Python 3 and without the help of any external dependencies, you shouldn't need to install anything (other than a Python 3.6+) in order to use it.



<!-- USAGE -->
## Usage

The general syntax to run the solver is:
```
python main.py -i <path-to-input-file>
```

or alternatively:
```
python main.py --input <path-to-input-file>
```

where `<path-to-input-file>` is (either absolute or relative) path to a file containing the Sudoku puzzle layout. 



<!-- SAMPLE SUDOKU PUZZLE -->
## Solving a Sample Sudoku Puzzle

There are currently 8 sample Sudoku puzzles available under the `sample_inputs` directory in this repository.

As an example, you may use the following command to solve the 3rd sample Sudoku puzzle:
```
python main.py -i ./sample_inputs/input3.txt
```

After running the above command, you should see the visual representation of the Sudoku puzzle on your screen:
```
               Puzzle
┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓
┃   │ 2 │   ┃ 6 │   │ 8 ┃   │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 5 │ 8 │   ┃   │   │ 9 ┃ 7 │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃   │ 4 │   ┃   │   │   ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃ 3 │ 7 │   ┃   │   │   ┃ 5 │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 6 │   │   ┃   │   │   ┃   │   │ 4 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │ 8 ┃   │   │   ┃   │ 1 │ 3 ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃   │   │   ┃   │ 2 │   ┃   │   │   ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │ 9 ┃ 8 │   │   ┃   │ 3 │ 6 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃ 3 │   │ 6 ┃   │ 9 │   ┃
┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛

Solving...
```

and just a few moments later, the solution for the Sudoku puzzle should pop up:
```
               Puzzle                                    Solution
┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓      ┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓
┃   │ 2 │   ┃ 6 │   │ 8 ┃   │   │   ┃      ┃ 1 │ 2 │ 3 ┃ 6 │ 7 │ 8 ┃ 9 │ 4 │ 5 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 5 │ 8 │   ┃   │   │ 9 ┃ 7 │   │   ┃      ┃ 5 │ 8 │ 4 ┃ 2 │ 3 │ 9 ┃ 7 │ 6 │ 1 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃   │ 4 │   ┃   │   │   ┃      ┃ 9 │ 6 │ 7 ┃ 1 │ 4 │ 5 ┃ 3 │ 2 │ 8 ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫      ┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃ 3 │ 7 │   ┃   │   │   ┃ 5 │   │   ┃      ┃ 3 │ 7 │ 2 ┃ 4 │ 6 │ 1 ┃ 5 │ 8 │ 9 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 6 │   │   ┃   │   │   ┃   │   │ 4 ┃      ┃ 6 │ 9 │ 1 ┃ 5 │ 8 │ 3 ┃ 2 │ 7 │ 4 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │ 8 ┃   │   │   ┃   │ 1 │ 3 ┃      ┃ 4 │ 5 │ 8 ┃ 7 │ 9 │ 2 ┃ 6 │ 1 │ 3 ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫      ┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃   │   │   ┃   │ 2 │   ┃   │   │   ┃      ┃ 8 │ 3 │ 6 ┃ 9 │ 2 │ 4 ┃ 1 │ 5 │ 7 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │ 9 ┃ 8 │   │   ┃   │ 3 │ 6 ┃      ┃ 2 │ 1 │ 9 ┃ 8 │ 5 │ 7 ┃ 4 │ 3 │ 6 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨      ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃   │   │   ┃ 3 │   │ 6 ┃   │ 9 │   ┃      ┃ 7 │ 4 │ 5 ┃ 3 │ 1 │ 6 ┃ 8 │ 9 │ 2 ┃
┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛      ┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛

Processing Time = 0.007 s
```


<!-- CUSTOM SUDOKU PUZZLE -->
## Solving a Custom Sudoku Puzzle

For solving a custom Sudoku puzzle create a text file with 9 lines, each representing a row of the Sudoku table. In each line, put 9 white-space-seperated valid values. Allowed values are digits 1 to 9 (for known Sudoku cells) and " - " hyphen (for unknown Sudoku cells).

In the following example you can see 9 lines, each containing 9 tab-seperated values, represeting a valid Sudoku puzzle for the solver:

```
-   -   -   2   6   -   7   -   1
6   8   -   -   7   -   -   9   -
1   9   -   -   -   4   5   -   -
8   2   -   1   -   -   -   4   -
-   -   4   6   -   2   9   -   -
-   5   -   -   -   3   -   2   8
-   -   9   3   -   -   -   7   4
-   4   -   -   5   -   -   3   6
7   -   3   -   1   8   -   -   -
```

After creating and saving the file, use the previously mentioned syntax to solve the puzzle.

<b>Note.</b> _As mentioned earler, this Sudoko solver utilizes a backtracking algorithm. Backtracking algorithms are known to be exponential in terms of time complexity, so it is possible to deliberately engineer a Sudoku puzzle, for which you will have to wait as long as a few minutes before the puzzle is solved._



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
