# tic_tac_toe/api.py
from flask import Flask, abort
from flask import request, jsonify
import requests

from .utilities import tic_tac_toe_winner

app = Flask(__name__)


@app.route('/winner', methods=['GET'])
def winner():
    board = request.args.get('board', '').replace('_', ' ')
    try:
        return jsonify({
            'winner': tic_tac_toe_winner(board)
        })
    except ValueError:
        abort(400)

@app.route('/winner_external', methods=['GET'])
def winner_external():
    if 'board' not in request.args:
        abort(400)
    board = request.args.get('board', '').replace('_', ' ')
    r = requests.get(f'https://api.github.com/tictactoe?board={board}')
    if r.status_code == 200:
        winner = r.text
    else:
        abort(502)
    try:
        return jsonify({
            'winner': winner
        })
    except ValueError:
        abort(400)