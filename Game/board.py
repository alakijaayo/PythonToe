class Board:


  def __init__(self):
    self.game = False
    self.options = ["TL", "TC", "TR", "ML", "MC", "MR", "BL", "BC", "BR"]
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
    self.winner()

  def userChoice(self, answer, user):
    position = answer.upper()
    if position in self.options:
      if self.choices[position] == " ":
        self.choices[position] = user
        self.print_board()
      elif self.choices[position] != " ":
        print("This position is already taken. Try again:")
        answer = input()
        self.userChoice(answer, user)
    else:
      print("Looks like that isn't a space on the board. Try again:")
      answer = input()
      self.userChoice(answer, user)
      

  def winner(self):
    win = [
      [self.choices["BC"], self.choices["BL"], self.choices["BR"]],
      [self.choices["BC"], self.choices["MC"], self.choices["TC"]],
      [self.choices["BL"], self.choices["MC"], self.choices["TR"]],
      [self.choices["BL"], self.choices["ML"], self.choices["TL"]],
      [self.choices["BR"], self.choices["MC"], self.choices["TL"]],
      [self.choices["BR"], self.choices["MR"], self.choices["TR"]],
      [self.choices["MC"], self.choices["ML"], self.choices["MR"]],
      [self.choices["TC"], self.choices["TL"], self.choices["TR"]]
    ]

    for x in win:
      if x[0] == "X" and x[1] == "X" and x[2] == "X":
        self.game = True
      elif x[0] == "O" and x[1] == "O" and x[2] == "O":
        self.game = True
    