from Game.board import Board

class Player:
  def __init__(self, name1 = "", name2 = ""): # would the defaults be necessary?
    self.name1 = name1
    self.name2 = name2
    self.board = Board()
  
  def player1_name(self): # These two methods are very similar
    print("Player 1 enter your name:")
    self.name1 = input()
    print("So player 1 your name is " + self.name1.capitalize())
  
  def player2_name(self):
    print("Player 2 enter your name:")
    self.name2 = input()
    print("And player 2 your name is " + self.name2.capitalize()) # I prefer the use of f-strings as oppose to string concatenation
  
  def move_X(self, answer): # these move methods can be removed and self.board.userChoice can be invoked directly with a player symbol
    self.board.userChoice(answer=answer, user="X")
  
  def move_O(self, answer):
    self.board.userChoice(answer=answer, user="O")