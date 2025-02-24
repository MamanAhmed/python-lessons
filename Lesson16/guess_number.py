import sys
import random


def gmn(name="PlayerOne"):
    game_count = 0
    player_wins = 0

    def play_gmn():
        nonlocal name
        nonlocal player_wins

        # Get user input
        player_guess = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n")

        # Validate user input
        if player_guess not in ["1", "2", "3"]:
            print(f"\n{name}, please guess a number between 1 and 3.\n")
            return play_gmn()

        # Get computer choice
        computer = random.choice((1, 2, 3))

        # Convert user input to int
        player = int(player_guess)

        # Print choices
        print(f"\n{name}, You chose {player}.")
        print(f"\nI was thinking about the number {computer}.")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time. 😿"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"Your winning percentage: {player_wins / game_count:.2%}%")

        # Ask user to play again

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for yes or \nQ to quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gmn()
        else:
            print("🎉🎉🎉🎉")
            print("\nThank you for playing!")
            if __name__ == "__main__":
                sys.exit(f"\nBye {name}! 👋🏾")
            else:
                return

    return play_gmn


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalised guess the number game"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    guessmynumber = gmn(args.name)
    guessmynumber()
