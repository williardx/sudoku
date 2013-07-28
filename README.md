sudoku
======
sudoku is a Sudoku puzzle solver. It contains `solver.py`, which processes Sudoku boards from a text file and then passes it to the Sudoku solver contained in `Sudoku.py`. Example boards are given in `boards`, including boards that produce one solution, no solution, and many solutions.

Input
-----
Sudoku input must be in the form a text file containing only the board. Columns are separated by commas and rows are separated by line returns. Missing numbers should be filled in with either 0's or nothing. E.g., the following are valid rows in a Sudoku board:

	0,0,2,0,4,1,0,0,0 
	,,2,,4,1,,,

Here's an example of a valid Sudoku board:

	0,5,6,9,0,7,4,0,0
	0,8,1,0,4,0,0,0,0
	0,0,0,0,1,5,0,9,0
	0,0,0,0,0,3,8,5,7
	8,4,0,0,6,0,0,2,3
	7,3,9,2,0,0,0,0,0
	0,6,0,5,8,0,0,0,0
	0,0,0,0,7,0,3,6,0
	0,0,8,3,0,6,5,7,0


If you give a Sudoku board with the wrong dimensions or with less than the minimum number of numbers to solve the puzzle (17), the program will complain.

Use
---

	python solver.py BOARD.txt

where `BOARD.txt` is the text file containing your comma-delimited Sudoku board.

Output
------
The output will tell you the number of solutions, the solutions, and the time it took to calculate the solutions. For example, here's the solution to board1.txt:

	1 solution found in 0.185677051544 seconds!

	n = 1

	2 5 6 9 3 7 4 8 1
	9 8 1 6 4 2 7 3 5
	4 7 3 8 1 5 6 9 2
	6 1 2 4 9 3 8 5 7
	8 4 5 7 6 1 9 2 3
	7 3 9 2 5 8 1 4 6
	3 6 7 5 8 4 2 1 9
	5 2 4 1 7 9 3 6 8
	1 9 8 3 2 6 5 7 4
