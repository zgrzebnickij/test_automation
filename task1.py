def tic_tac_toe_winner(board):
    for i in range(3):
        #cols
        if board[i] == board[i+3] == board[i+6] and board[i] in ['X', 'O']:
            return board[i]
        #rows
        if board[i*3] == board[1 + 3*i] == board[2 + 3*i] and board[i*3] in ['X', 'O']:
            return board[i*3]
        #cros
        if board[0] == board[4] == board[8] and board[0] in ['X', 'O']:
            return board[0]
        #cros
        if board[2] == board[4] == board[6] and board[2] in ['X', 'O']:
            return board[2]

test_cases = {
    'XO  X O X': 'X',
    'OX  O X O': 'O',
    'XXOOXXXOO': None,
}

for board, expectation in test_cases.items():
    response = tic_tac_toe_winner(board)
    assert response == expectation, \
        f'Expected {expectation!r} for {board!r} got {response!r}'