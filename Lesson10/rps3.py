import sys
import random
from enum import Enum

# Rock, Paper, Scissors Game


def play_rps():
    # Define Enum class
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Get user input
    playerchoice = input(
        "\nEnter... \n1 for Rock\n2 for Paper\n3 for Scissors:\n\n")

    # Validate user input
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter a number between 1 and 3")
        return play_rps()

    # Convert user input to integer
    player = int(playerchoice)

    # Get computer choice
    computerchoice = random.choice("123")

    # Convert computer choice to integer
    computer = int(computerchoice)

    # Print choices
    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    # Determine winner
    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")

    # Ask user to play again
    print("\n Play again?")
    while True:
        playagain = input("\nY for Yes or \n Q to Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thanks for playing!\n")
        sys.exit("Bye! 👋🏾")


play_rps()
