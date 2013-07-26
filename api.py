from flask import Flask
from flask.ext.restful import reqparse, Api, Resource
import os

app = Flask(__name__)
api = Api(app)

def txt_to_board(f):
    board = []
    o = open(f, 'r')
    for line in o:
        line.strip("\n")
        line_list = line.split(",")
        line_list = map(int, line_list)
        board.append(line_list)
    o.close()
    return board

def generate_boards_list(folder='./boards'):
    boards = {}
    for f in os.listdir(folder):
        if os.path.isfile(f):
            boards[f.strip(".txt")] = txt_to_board(f)
    return boards

BOARDS = generate_boards_list()

parser = reqparse.RequestParser()
parser.add_argument('elt', type=int)
parser.add_argument('i', type=int)
parser.add_argument('j', type=int)

class Board(Resource):

    def get(self, board_id):
        return BOARDS[board_id]

    def put(self, board_id):
        args = parser.parse_args()
        elt = args['elt']
        i = args['i']
        j = args['j']
        BOARDS[board_id][i][j] = elt
        return BOARDS[board_id], 201

class BoardList(Resource):
    def get(self):
        return BOARDS

api.add_resource(BoardList, '/boards')
api.add_resource(Board, '/boards/<string:board_id>')

if __name__ == '__main__':
    app.run(debug=True)
