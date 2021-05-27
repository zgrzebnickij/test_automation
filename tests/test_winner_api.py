# tests/test_winner_api.py
from requests import status_codes
from tic_tac_toe.api import app
from os import close, unlink
from tempfile import mkstemp
from itertools import count
from sqlalchemy import create_engine
from unittest.mock import Mock
import pytest
import csv

from tic_tac_toe.database import winner, metadata, history

def test_api_is_wsgi_app():
    assert hasattr(app, 'wsgi_app')

def test_api_missing_parameter():
    assert app.test_client().get('/winner').status_code == 400

def test_api_response_is_json():
    response = app.test_client().get('/winner?board=_________')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert 'winner' in response.json

@pytest.fixture
def create_games(database_connection):

    def game_creator(*games):
        move_id = count(1)
        for game_id, moves in enumerate(games, 1):
            database_connection.execute(history.insert(), [
                {
                    'game_id': game_id,
                    'move_id': next(move_id),
                    'position': int(position),
                    'symbol': symbol
                } for position, symbol in zip(moves[::2], moves[1::2])
            ])

    return game_creator


@pytest.fixture
def database_connection():
    fd, name = mkstemp(prefix='test_winner_', suffix='.sqlite')
    engine = create_engine(f'sqlite:///{name}')
    metadata.create_all(engine)
    with engine.connect() as connection:
        yield connection
    close(fd)
    unlink(name)

@pytest.fixture
def load_test_cases_from_file():
    with open('tests/test_cases.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        yield csv_reader

@pytest.fixture
def connection_mock():
    return lambda moves: Mock(
        execute=Mock(
            return_value=[
                (int(position), symbol)
                for position, symbol
                in zip(moves[::2], moves[1::2])
            ]
        )
    )

def test_create_board_from_moves(connection_mock, monkeypatch):
    monkeypatch.setattr(
        'tic_tac_toe.database.tic_tac_toe_winner',
        lambda board: board
    )
    assert winner(connection_mock('4X1O5X3O2X6O8X'), None) == ' OXOXXO X'


def test_3x_in_a_column_with_mock(connection_mock):
    assert winner(connection_mock('4X1O5X3O2X6O8X'), None) == 'X'


@pytest.mark.parametrize("test_input,expected", [('4X1O5X3O2X6O8X', 'X'), ('4O1X5O3X2O6X8O', 'O')])
def test_3x_in_a_column(database_connection, create_games, test_input, expected):
    create_games(test_input)
    assert winner(database_connection, 1) == expected

### testing function which requre request to external api

def test_api_missing_parameter():
    assert app.test_client().get('/winner_external').status_code == 400

def test_api_response_error_from_external(monkeypatch):
    monkeypatch.setattr(
        'tic_tac_toe.api.requests',
        Mock(
            get=Mock(
                return_value=Mock(
                    status_code=502,
                    text='X'
                )
            )
        )
    )
    response = app.test_client().get('/winner_external?board=_________')
    assert response.status_code == 502

def test_api_response_is_json(monkeypatch):
    monkeypatch.setattr(
        'tic_tac_toe.api.requests',
        Mock(
            get=Mock(
                return_value=Mock(
                    status_code=200,
                    text='X'
                )
            )
        )
    )
    response = app.test_client().get('/winner_external?board=_________')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert 'winner' in response.json