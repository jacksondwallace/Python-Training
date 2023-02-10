import random
import sys

user = ""
computer = ""

def start__game():
    # Select Inputs
    user = input("What's your choice? Rock, Paper or Scissors ")
    computer = random.choice(['Rock', 'Paper', 'Scissors'])

    # User Picks Rock
    if user == "Rock" and computer == "Rock":
        print("It's a draw! You both selected Rock")
    elif user == "Rock" and computer == "Paper":
        print("Computer selected Paper and won!")
    elif user == "Rock" and computer == "Scissors":
         print("Computer selected Paper, You win!")

    # User Picks Paper
    if user == "Paper" and computer == "Paper":
        print("It's a draw! You both selected Paper")
    elif user == "Paper" and computer == "Rock":
        print("Computer selected Rock, You win!")
    elif user == "Paper" and computer == "Scissors":
         print("Computer selected Scissors and won!")

    # User Picks Scissors
    if user == "Scissors" and computer == "Paper":
        print("User wins")
    elif user == "Scissors" and computer == "Rock":
        print("Computer wins")
    elif user == "Scissors" and computer == "Scissors":
         print("It's a draw")

    play__again = input("Would you like to play again? Yes or No ")
    if play__again == "Yes":
        start__game()
    else:
        sys.exit()

def clear__game():
    user = ""
    computer = ""

start__game()

