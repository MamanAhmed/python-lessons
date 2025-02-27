import sys
import random
from enum import Enum

# Rock, Paper, Scissors Game


def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        # Define Enum class
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Get user input
        playerchoice = input(
            f"\n{name}, please enter... \n1 for Rock\n2 for Paper\n3 for Scissors:\n\n")

        # Validate user input
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please you must enter a number between 1 and 3")
            return play_rps()

        # Convert user input to integer
        player = int(playerchoice)

        # Get computer choice
        computerchoice = random.choice("123")

        # Convert computer choice to integer
        computer = int(computerchoice)

        # Print choices
        print(f"\n{name}, you chose {str(RPS(player)).replace("RPS.", "")}.")
        print(f"Python chose {str(RPS(computer)).replace("RPS.", "")}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}...😿 "

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        # Ask user to play again
        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thanks for playing!\n")
            sys.exit(f"Bye {name}! 👋🏾")
    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized Rock-Paper-Scissor game."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
