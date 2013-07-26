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
        line.strip("\n")
        line_list = line.split(",")
        line_list = map(int, line_list)
        board.append(line_list)
    o.close()
    return board

def generate_boards_list(path='./boards'):
    '''
    Generate list of boards given directory containing text files
    '''
    boards = {}
    for f in os.listdir(path):
        boards[f.strip(".txt")] = txt_to_board(path + '/' + f)
    return boards

BOARDS = generate_boards_list()
USERS = {}

parser = reqparse.RequestParser()
parser.add_argument('elt', type=int)
parser.add_argument('i', type=int)
parser.add_argument('j', type=int)
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
        return USERS[user_id][board_id]

    def put(self, user_id, board_id):
        args = parser.parse_args()
        elt = args['elt']
        i = args['i']
        j = args['j']
        USERS[user_id][board_id][i][j] = elt
        return USERS[user_id][board_id], 201

class BoardList(Resource):

    def get(self, user_id):
        return USERS[user_id]

api.add_resource(UserList, '/users/')
api.add_resource(BoardList, '/users/<string:user_id>/boards/')
api.add_resource(Board, '/users/<string:user_id>/boards/<string:board_id>')

if __name__ == '__main__':
    app.run(debug=True)
