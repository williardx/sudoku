#!/usr/local/bin/python

from sudoku import Sudoku
from numpy import matrix
from sys import argv
from time import time

script, f = argv

def txt_to_matrix(f):
    '''
    Takes input file containing Sudoku board
    and produces a matrix
    '''
    line_arr = []
    o = open(f, 'r')
    for line in o:
        line.strip("\n")
        line_arr.append(" ".join(line.split(",")))
    mat = matrix((";".join(line_arr)))
    o.close()
    return mat

def check_min_board(mat):
    '''
    Check if matrix has minimum number of numbers for a Sudoku puzzle
    '''
    count = 0
    for i in range(9):
        for j in range(9):
            if mat[i,j] != 0:
                count += 1
    return count >= 17

def process_file(f):
    '''
    Processes a Sudoku board from file f and returns a solution along with calculation time.
    '''
    mat = txt_to_matrix(f)
    if len(mat) != 9: #make sure given board is 9 x 9
        print "Invalid Sudoku board! Incorrect dimensions."
    elif not check_min_board(mat): #make sure matrix has minimum number of numbers
        print "Invalid Sudoku board! Not enough numbers for a solution."
    else:
        puzzle = Sudoku(mat)
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
                print str(answers[i]) + ("" if len(answers)==1 else "\n")

if __name__ == "__main__":
    process_file(f)
