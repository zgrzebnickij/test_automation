# tic_tac_toe/api.py
from flask import Flask

from .utilities import tic_tac_toe_winner

app = Flask(__name__)

@app.route('/winner', methods=['GET'])
def winner():
    abort(400)