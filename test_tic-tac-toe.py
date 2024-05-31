from tic_tac_toe_ET import evaluate, move

def test_evaluate():
    board1 = "-------xxx----------"
    assert evaluate(board1) == "x"
    board2 = "ooo-----------------"
    assert evaluate(board2) == "o"
    board3 = "xxooxxoxxoxoxoxoxoxo"
    assert evaluate(board3) == "Draw"

def test_move():
    board1 = "--------------------"
    move1 = move(board1, 'x', 1)
    assert move1 == "-x------------------"
    board2 = "--------------------"
    move2 = move(board2, 'o', 19)
    assert move1 == "-------------------o"

