from Game.player import Player

player1 = Player()
player2 = Player()

def player1_name():
  print("Player 1 enter your name:")
  player1.name = input()
  print("Welcome, " + player1.name)

def player2_name():
  print("Player 2 enter your name, or put 'Com' to face me:")
  player2.name = input()
  

def start():
  print("Welcome to Tic Tac Toe/Noughts and Crosses!")
  print("This is a two player game")
  print("To pick a square, please put the initials. For example, bottom left will be 'BL'")
  print("Let's Begin!")
  player1_name()
  player2_name()

start();