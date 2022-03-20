from Game.player import Player

player = Player()

def player_1_move():
  print("Player 1, choose your position:")
  answer = input()
  player.move_X(answer=answer)

def player_2_move():
  print("Player 2, choose your position:")
  answer = input()
  player.move_O(answer=answer)

def start():
  print("Welcome to Tic Tac Toe/Noughts and Crosses!")
  print("This is a two player game")
  print("To pick a square, please put the initials. For example, bottom left will be 'BL'")
  print("Let's Begin!")
  player.player1_name()
  player.player2_name()
  i = 0
  while True:
    player_1_move()
    i += 1
    if player.board.game == True:
      print(player.name1.capitalize() + " Wins!")
      break
    if i == 9:
      print("It's a Draw")
      break
    player_2_move()
    i += 1
    if player.board.game == True:
      print(player.name2.capitalize()  + " Wins!")
      break

start();