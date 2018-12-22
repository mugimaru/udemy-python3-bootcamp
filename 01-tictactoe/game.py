def next_player(current):
  if current == 'X':
    return 'O'
  else:
    return 'X'

def print_board(board):
  print(" {} | {} | {}\n-----------\n {} | {} | {}\n-----------\n {} | {} | {}".format(*[v or i + 1 for i, v in enumerate(board)]))

def ask_turn(board, current_player, available_choices):
  inp = input(f"Player {current_player} turn: ")

  if inp in available_choices:
    return int(inp) - 1
  else:
    return ask_turn(board, current_player, available_choices)

def play():
  current_player = 'X'
  winner = None
  board = [None] * 9

  while winner == None:
    print_board(board)
    next_turn = ask_turn(board, current_player, [str(i + 1) for (i, value) in enumerate(board) if value == None])

    board[next_turn] = current_player
    current_player = next_player(current_player)

    winner = find_winner(board)

  if ask_replay(winner):
    play()

def canidates(b):
  l = [b[0:9:4], b[2:8:2]]
  for n in range(0, 2):
    l.append(b[n*3:(n+1)*3])
    l.append(b[n:9:3])

  return l

def find_winner(board):
  for c in canidates(board):
    if c == ['X', 'X', 'X']:
      return 'X'
    elif  c == ['O', 'O', 'O']:
      return 'O'

  return None

def ask_replay(winner):
  return input(f"Player {winner} has won. Replay? Yes/No:\n") == 'Yes'

play()