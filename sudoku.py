from numpy import matrix
from copy import copy

class Sudoku:

    def __init__(self, mat):
        
        self.board = mat #Sudoku class takes in matrix as board
        #blocks are the 3 x 3 submatrices that must each uniquely contain numbers 1 - 9
        self.blocks = [[self.board[0:3, 0:3], self.board[0:3, 3:6], self.board[0:3, 6:9]], \
                       [self.board[3:6, 0:3], self.board[3:6, 3:6], self.board[3:6, 6:9]], \
                       [self.board[6:9, 0:3], self.board[6:9, 3:6], self.board[6:9, 6:9]]]

    def __str__(self):
        rows_list = []
        for row in self.board:
                rows_list.append(str(row).strip('[[]]'))
        return "\n".join(rows_list)

    def check_row(self, elt, index):
        '''
        Check if element is in row i for index (i,j)
        '''
        return elt in self.board[index[0]]

    def check_col(self, elt, index):
        '''
        Check if element is in in column j for index (i,j)
        '''
        return elt in self.board[:,index[1]]

    def check_block(self, elt, index):
        '''
        Check if element is in block containing (i,j)th index
        '''
        return elt in self.blocks[index[0] // 3][index[1] // 3]

    def element_is_valid(self, elt, index):
        '''
        Check if element at index (i,j) violates board rules
        '''
        row = self.check_row(elt, index)
        col = self.check_col(elt, index)
        bl = self.check_block(elt, index)
        return (not row) and (not col) and (not bl)

    def is_solved(self):
        '''
        Check if the board is solved
        '''
        if 0 in self.board:
            return False
        else:
            return True

    def find_index(self, elt):
        '''
        Search for first occurrence of element in board
        '''
        for i in range(9):
            for j in range(9):
                if self.board[i,j] == elt:
                    return (i,j)

    def solve_board(self):
        '''
        Solve Sudoku board
        '''

        if self.is_solved():
            return [Sudoku(self.board)]
        else:
            numbers = range(1,10)
            #find entry with lowest index in matrix containing 0
            index = self.find_index(0)
            new_boards = []
            #generate list of valid new boards substituting in numbers 1-9 for 0 at given index
            #and store in list new_boards
            for num in numbers:
                if self.element_is_valid(num, index):
                    self.board[index] = num
                    new_boards.append(Sudoku(copy(self.board)))
                    self.board[index] = 0
            if new_boards == []:
                return []
            else:
                #apply solve_board to valid boards in list and concatenate together answer lists
                #(either [] or [board]) to generate list of answers
                return reduce(list.__add__, [board.solve_board() for board in new_boards])
