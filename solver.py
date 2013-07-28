#!/usr/local/bin/python

from sudoku import Sudoku
from numpy import matrix, int64
from sys import argv
from time import time

script, f = argv

def txt_to_board(f):
    '''
    Takes input file containing Sudoku board
    and produces a Sudoku board object
    '''
    line_list = []
    o = open(f, 'r')
    try:
        #Parse file
        for line in o:
            line = line.strip("\n")
            line_chars = line.split(",")
            for i in range(len(line_chars)):
                if line_chars[i] == "":
                    line_chars[i] = '0'
            line_list.append(" ".join(line_chars))
        mat = matrix((";".join(line_list)))
        o.close()
                
        #board must be a 9 x 9 grid
        if mat.shape != (9,9):
            raise ValueError

        #numbers must be integers 0 - 9
        if not check_cell_contents(mat):
            raise ValueError

        #board must have at least 17 filled-in numbers
        if not check_min_board(mat):
            raise ValueError
        
        return Sudoku(mat)

    except (ValueError, SyntaxError):
        return False

def check_cell_contents(mat):
    '''
    Check if matrix has correct values for Sudoku puzzle
    '''
    for i in range(9):
        for j in range(9):
            elt = mat[i,j]
            if (elt > 9) or (elt < 0) or (type(elt) != int64):
                return False
    return True

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
    Processes a Sudoku board from file f and returns a solution along with
    calculation time.
    '''
    
    puzzle = txt_to_board(f)
    
    if puzzle is False:
        print "\nInvalid input -- make sure the Sudoku board is 9 x 9, " \
                "contains only numbers 0-9, and that at least 17 cells " \
                "are filled in. Here's an example of a valid Sudoku " \
                "input board:\n\n \
                0,5,6,9,0,7,4,0,0\n \
                0,8,1,0,4,0,0,0,0\n \
                0,0,0,0,1,5,0,9,0\n \
                0,0,0,0,0,3,8,5,7\n \
                8,4,0,0,6,0,0,2,3\n \
                7,3,9,2,0,0,0,0,0\n \
                0,6,0,5,8,0,0,0,0\n \
                0,0,0,0,7,0,3,6,0\n \
                0,0,8,3,0,6,5,7,0\n"

    else:
        t_i = time()
        answers = puzzle.solve_board()
        t_f = time()
        dt = t_f - t_i
        if len(answers) == 0:
            print "\nSorry, no solutions were found."
            print "Total calculation time was " + str(dt) + " seconds\n"
        else:
            print "\n"+str(len(answers)) + " solution" +  \
                  ("" if len(answers)==1 else "s") + \
                  " found in " + str(dt) + " seconds!\n"
            for i in range(len(answers)):
                print "n = " + str(i+1) + "\n"
                print str(answers[i]) + "\n"

if __name__ == "__main__":
    process_file(f)
