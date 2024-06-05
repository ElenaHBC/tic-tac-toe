from tic_tac_toe_ET import evaluate, move

def test_evaluate_x():
    board = "-------xxx----------"
    assert evaluate(board) == "x"

def test_evaluate_o():
    board = "ooo-----------------"
    assert evaluate(board) == "o"

def test_evaluate_draw():
    board = "xxooxxoxxoxoxoxoxoxo"
    assert evaluate(board) == "Draw"

def test_move_x():
    board = "--------------------"
    move_x = move(board, 'x', 1)
    assert move_x == "-x------------------"

def test_move_o():
    board = "--------------------"
    move_o = move(board, 'o', 19)
    assert move_o == "-------------------o"

"""
a) python module is an organized block/box of code, while packages contain several modules with sub-modules
b) side effects of modules are undesirable effects when calling/importing the module, for example if the module contains print statements
c) exceptions are error messages that have a specific information for the art of error; there are several hierarchial built-in exceptions;
What to do if third-party code that we use throws exceptions? - I guess we either correct the code or catch the exceptions with except?
d) create, throw and catch exceptions: raise (creates and throws), try, except (catches and handles an error), else, 
finally (mostly for clean-ups), class to create your own definition of a custom exception based on some built-in exception 
e) examples of benefits of testing - I guess checking if the code works properly can be done faster and more efficiently;
also you can "prove' to others that the code works as expected

Since I missed lesson nr.11 and had to catch up on my own, I had some problems with the homework and some unclarity regarding 
testing and raising/catching errors. I tried to use the ValueError for the tic-tact-toe game in player_move function to catch a not numerical
user input but it doesn't work and I am not sure how to do this properly.
Also testing did not work for all of the exercises from the lesson and I need more time to go over everything again. 
"""