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
    assert move2 == "-------------------o"

"""
a) python module is an organized block/box of code, while packages contain several modules with sub-modules
b) side effects of modules are undesirable effects when calling/importing the module, for example if the module contains print statements
c) exceptions are error messages that have a specific information for the art of error; there are several hierarchial built-in exceptions;
What to do if third-party code that we use throws exceptions? - I guess we either correct the code or catch the exceptions with except?
d) create, throw and catch exceptions: raise (creates and throws), try, except (catches and handles an error), else, finally (mostly for clean-ups)?
e) examples of benefits of testing - I guess checking if the code works properly can be done faster and more efficiently;
also you can "prove' to others that the code works as expected

Since I missed lesson nr.11 and had to catch up on my own, I had some problems with the homework and some unclarity regarding 
testing and raising/catching errors. I tried to use the ValueError for the tic-tact-toe game in player_move function to catch a not numerical
user input but it doesn't work and I am not sure how to do this properly.
Also testing did not work for all of the exercises from the lesson and I need more time to go over everything again. 
"""