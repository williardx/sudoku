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
    ans = []
    o = open(f, 'r')
    for line in o:
        line.strip("\n")
        ans.append(" ".join(line.split(",")))
    board = matrix((";".join(ans)))
    return Sudoku(board)

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
    for the Sudoku puzzle
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


def main(f):
    '''
    Main procedure for the Sudoku solver
    Solves Sudoku puzzle, calculates calculation time,
    and prints out the solutions
    '''
    puzzle = txt_to_board(f)
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
