from random import randrange
board = ("--------------------")

def evaluate(board):
  if "xxx" in board:
    return "x"
  elif "ooo" in board:
    return "o"
  elif "-" not in board:
    return "Draw"
  else:
    return None

def move(board, mark, position):
  return board[:position] + mark + board[position + 1:]

def player_move(board):
  while True:
    user_input = int(input("Which position between 1 and 20 do you want to play?: "))
    if 0 < user_input <= 20:
      user_move = user_input - 1
      if board[user_move] == "-":
        return move(board, "x", user_move)
      else:
        print("Please choose an empty position on the board.")
    else:
      print("Please enter a number between 1 and 20.")

def pc_move(board):
  while True:
    pc_mark_move = randrange(20)
    if board[pc_mark_move] == "-":
      return move(board, "o", pc_mark_move)

def tictactoe_1D():
  board = ("--------------------")
  player = "x"

  while True:
    print(board)
    if player =="x":
      board = player_move(board)
    else:
      board = pc_move(board)

    if evaluate(board) == "Draw":
      print(board)
      print("It's a draw!")
      break
    elif evaluate(board) == "x":
       print(board)
       print("X wins!")
       break
    elif evaluate(board) == "o":
       print(board)
       print("O wins!")
       break

    if player == "x":
      player = "o"
    else: player = "x"

tictactoe_1D()
