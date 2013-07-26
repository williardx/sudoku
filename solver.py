#!/usr/local/bin/python

from sudoku import Sudoku
from numpy import matrix
from sys import argv
from time import time

script, f = argv

def txt_to_board(f):
    '''
    Takes input file containing Sudoku board
    and produces a Sudoku object
    '''
    line_arr = []
    o = open(f, 'r')
    for line in o:
        line.strip("\n")
        line_arr.append(" ".join(line.split(",")))
    board = matrix((";".join(line_arr)))
    o.close()
    return board

def make_readable_solution(mat):
    '''
    Converts matrix to a human-readable string
    '''
    ans = []
    for row in mat:
        ans.append(row.__str__().strip('[[]]'))
    return "\n".join(ans)

def convert_format(f):
    '''
    Simple function that converts between formats
    I initially used and Codecademy wanted for the Sudoku puzzle
    '''
    ans = ""
    o = open(f, 'r+')
    for line in o:
        line = line.strip("\n")
        line = ",".join(line.split(" ")) + "\n"
        ans += line
    o.seek(0)
    o.write(ans)
    o.truncate()
    o.close()

def check_min_board(board):
    '''
    Check if board has minimum number of numbers for a Sudoku puzzle
    '''
    count = 0
    for i in range(9):
        for j in range(9):
            if self.board[i,j] != 0:
                count += 1
    return count >= 17

def main(f):
    '''
    Main procedure for the Sudoku solver
    Solves Sudoku puzzle, calculates calculation time,
    and prints out the solutions
    '''
    board = txt_to_board(f)
    if len(board) != 9: #make sure given board is 9 x 9
        print "Invalid Sudoku board! Incorrect dimensions."
    elif not check_min_board(): #make sure board has minimum number of numbers
        print "Invalid Sudoku board! Not enough numbers for a solution."
    else:
        puzzle = Sudoku(board)
        t_i = time()
        answers = puzzle.solve_board()
        t_f = time()
        dt = (t_f - t_i)
        if len(answers) == 0:
            print "Sorry, no solutions were found."
            print "Total calculation time was " + str(dt) + " seconds"
        else:
            print str(len(answers)) + " solution" + ("" if len(answers)==1 else "s") + \
                  " found in " + str(dt) + " seconds!\n"
            for i in range(len(answers)):
                print "n = " + str(i+1) + "\n"
                print make_readable_solution(answers[i]) + ("" if len(answers)==1 else "\n")

main(f)
