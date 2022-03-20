class Board:

  def __init__(self):
    self.choices = {
      "TL": " ",
      "TC": " ",
      "TR": " ",
      "ML": " ",
      "MC": " ",
      "MR": " ",
      "BL": " ",
      "BC": " ",
      "BR": " "
    }

  def print_board(self):
    print("   L   C   R")
    print(f'T  {self.choices["TL"]} | {self.choices["TC"]} | {self.choices["TR"]} ')
    print("  ---|---|---")
    print(f'M  {self.choices["ML"]} | {self.choices["MC"]} | {self.choices["MR"]} ')
    print("  ---|---|---")
    print(f'B  {self.choices["BL"]} | {self.choices["BC"]} | {self.choices["BR"]} ')
  
  def available(self, position):
    self.choices[position] == " "

  def userChoice(self, answer, user):
    if self.available(answer):
      self.choices[answer] = user
    elif self.available == False:
      print("This position is already taken. Try again:")
      answer = input()
      self.userChoice(answer, user)
  
  
    