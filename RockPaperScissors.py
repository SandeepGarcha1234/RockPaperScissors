import random

def rock_paper_scissors():
  player_choice = input("Please enter 'rock', 'paper' or 'scissors' (eg. rock): ")
  comp_choice = random.choice(['rock','paper','scissors'])
  print("The computer chooses", comp_choice)
  if (player_choice,comp_choice) in [('rock','scissors'),('scissors','paper'),('paper','rock')]:
    print("You win!")
  elif (player_choice,comp_choice) in [('rock','rock'),('scissors','scissors'),('paper','paper')]:
    print("It is a tie")
  else:
    print("Sorry, you lose. Better luck next time!")

while True:
  rock_paper_scissors()
  char = input("Would you like to play again? (y/n): ")
  while char not in ['y','n']:
    char = input("Would you like to play again? (y/n): ")
  if char=='n':
    break