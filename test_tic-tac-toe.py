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

"""
a) python module is an organized block/box of code, while packages contain several modules with sub-modules
b) side effects of modules are undesirable effects when calling/importing the module, for example if the module contains print statements
c) exceptions
d) create, throw and catch exceptions
e) examples of benefits of testing
"""