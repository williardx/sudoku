'''
RESTful web API built to allow players to interact with a Sudoku board
and make moves on a Sudoku board. The script searches for Sudoku boards
in text files located inside of "./boards/" and automatically adds them
to the list of available boards for the user. The name of the board file
is used as the board's ID.

Look at list of current users: curl http://localhost:5000/users/

Add a user: curl http://localhost:5000/users/ -d "user_id=(name)" -X POST

Delete a user: curl http://localhost:5000/users/user_id -X DELETE

Look at user's Sudoku boards: curl http://localhost:5000/users/user_id/boards/

Look at board boardx that user is playing: curl http://localhost:5000/users/user_id/boards/boardx

Modify user's board boardx by replacing contents of cell row = i and column = j with element num:
    curl http://localhost:5000/users/user_id/boards/boardx -d "elt=num&row=i&col=j" -X PUT


For example, if user "Will" wants to change cell (2,5) of Sudoku board board1 to have a value of 5, s/he might write:
    curl http://localhost:5000/users/Will/boards/board1 -d "elt=5&row=2&col=5" -X PUT

'''


from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
import os, copy

app = Flask(__name__)
api = Api(app)

def txt_to_board(f):
    '''
    Generate board as 2d array from text file input
    '''
    board = []
    o = open(f, 'r')
    for line in o:
        line = line.strip("\n")
        line_list = line.split(",")
        for i in range(len(line_list)):
            if line_list[i] == '':
                line_list[i] = '0'
        line_list = map(int, line_list)
        board.append(line_list)
    o.close()
    return board

def generate_boards_list(path='./boards/'):
    '''
    Generate list of boards given directory containing text files
    '''
    boards = {}
    for f in os.listdir(path):
        boards[f.strip(".txt")] = txt_to_board(path + f)
    return boards

BOARDS = generate_boards_list()
USERS = {}

parser = reqparse.RequestParser()
parser.add_argument('elt', type=int)
parser.add_argument('row', type=int)
parser.add_argument('col', type=int)
parser.add_argument('user_id', type=str)

class UserList(Resource):

    def get(self):
        return USERS.keys()
    
    def post(self):
        args = parser.parse_args()
        user_id = args['user_id']
        USERS[user_id] = copy.deepcopy(BOARDS)
        return 201

class User(Resource):

    def get(self, user_id):
        if user_id not in USERS:
            abort(404, message="User doesn't exist.")
        else:
            return USERS[user_id]

    def delete(self, user_id):
        if user_id not in USERS:
            abort(404, message="User doesn't exist.")
        else:
            del USERS[user_id]
            return '', 204

class Board(Resource):

    def get(self, user_id, board_id):
        if board_id not in BOARDS:
            abort(404, message="Board does not exist.")
        else:
            return USERS[user_id][board_id]

    def put(self, user_id, board_id):
        if board_id not in BOARDS:
            abort(404, message="Board does not exist.")
        else:
            args = parser.parse_args()
            elt = args['elt']
            row = args['row']
            col = args['col']
            USERS[user_id][board_id][row][col] = elt
            return USERS[user_id][board_id], 201

class BoardList(Resource):
    
    def get(self, user_id):
        if user_id not in USERS:
            abort(404, message="User does not exist.")
        else:
            return USERS[user_id]

api.add_resource(UserList, '/users/')
api.add_resource(User, '/users/<string:user_id>')
api.add_resource(BoardList, '/users/<string:user_id>/boards/')
api.add_resource(Board, '/users/<string:user_id>/boards/<string:board_id>')

if __name__ == '__main__':
    app.run(debug=True)
