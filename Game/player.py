from Game.board import Board

class Player:

  def __init__(self, name1 = "", name2 = ""):
    self.name1 = name1
    self.name2 = name2
    self.board = Board()
  

  def player1_name(self):
    print("Player 1 enter your name:")
    self.name1 = input()
  
  def player2_name(self):
    print("Player 2 enter your name")
    self.name2 = input()
  
  def move_X(self, answer):
    self.board.userChoice(answer=answer, user="X")
  
  def move_O(self, answer):
    self.board.userChoice(answer=answer, user="O")