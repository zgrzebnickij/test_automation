from tic_tac_toe.utilities import tic_tac_toe_winner

def test_import_tic_tac_toe_winner():
    try:
        from tic_tac_toe.utilities import tic_tac_toe_winner  #➜ 1
        assert callable(tic_tac_toe_winner), "tic_tac_toe not callable"  #➜ 2
    except ImportError as error:  #➜ 3
        assert False, error

def test_empty_board():
    assert tic_tac_toe_winner(' ' * 9) is None

def test_3x_in_a_row():
    winner = tic_tac_toe_winner('XXX O O  ')
    assert winner == 'X', f"expected X, got {winner}"

def test_3x_in_a_col():
    winner = tic_tac_toe_winner('XOXXO X O')
    assert winner == 'X', f"expected X, got {winner}"

def test_illegal_board_symbols():
    try:
        tic_tac_toe_winner('Ala ma kota')
        assert False, "ValueError expected"
    except ValueError:
        pass

def test_illegal_board_game():
    try:
        tic_tac_toe_winner('XXX O    ')
        assert False, "ValueError expected"
    except ValueError:
        pass

def test_illegal_board_size():
    try:
        tic_tac_toe_winner('XXX')
        assert False, "ValueError expected"
    except ValueError:
        pass

def test_no_winner():
    winner = tic_tac_toe_winner('XOXOXOOXO')
    assert winner == None, f"expected None, got {winner}"

def test_3x_in_diagonal():
    winner = tic_tac_toe_winner('XO OX O X')
    assert winner == 'X', f"expected X, got {winner}"

def test_3x_in_diagonal_2():
    winner = tic_tac_toe_winner(' OXOX X O')
    assert winner == 'X', f"expected X, got {winner}"


if __name__ == '__main__':
    for test in (
        test_import_tic_tac_toe_winner,
        test_empty_board,
        test_3x_in_a_row,
        test_3x_in_a_col,
        test_illegal_board_symbols,
        test_illegal_board_size,
        test_3x_in_diagonal,
        test_3x_in_diagonal_2,
        test_illegal_board_game,
        test_no_winner
    ):  #➜ 4
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)