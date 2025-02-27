import sys
from guess_number import gmn
from rps9 import rps


def play_game(name="PlayerOne"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu")

        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissor\n2 = Guess my number\n\nOr press \"x\" to exit the Arcade\n\n")

        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2 or x.")
            return play_game(name)

        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = gmn(name)
            guess_my_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋🏾")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized arcade experiece"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the arcade."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the arcade! 🕹️")

    arcade = play_game(args.name)
    arcade()
