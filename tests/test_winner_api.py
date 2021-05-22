# tests/test_winner_api.py
from tic_tac_toe.api import app

def test_api_is_wsgi_app():
    assert hasattr(app, 'wsgi_app')

def test_api_missing_parameter():
    assert app.test_client().get('/winner').status_code == 400