from random import randint


# A custom exception to handle one of the invalid inputs.
class TooManyPencilsTaken(Exception):
    pass


def ask_number_of_pencils():
    while True:
        try:
            pencils = int(input("How many pencils would you like to use:\n"))
            if pencils <= 0:
                print("The number of pencils should be positive.")
            else:
                return pencils
        except ValueError:
            print("The number of pencils should be an integer.")


def determine_first_player():
    while True:
        first_player = input(f"Who will be the first ({player}, {bot}):\n")
        if first_player.lower() in (player.lower(), bot.lower()):
            return first_player.capitalize()
        else:
            print(f"Choose between {player} and {bot}.")


def print_pencils(pencils):
    print(pencils * "|")


def bot_move(pencils):
    # Behaviour in a losing position.
    if pencils == 1:
        return 1
    elif pencils % 4 == 1:
        return randint(1, 3)

    # Behaviour in a winning position.
    elif pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1


def switch_player(current_player):
    return player if current_player == bot else bot


def play_game(pencils, current_player):
    while pencils > 0:
        try:
            print_pencils(pencils)
            print(f"{current_player}'s turn:")

            if current_player == bot:
                pencils_to_remove = bot_move(pencils)
                print(pencils_to_remove)

            else:
                pencils_to_remove = int(input())
                if pencils_to_remove not in range(1, 4):
                    raise ValueError
                elif pencils_to_remove > pencils:
                    raise TooManyPencilsTaken

            pencils -= pencils_to_remove
            current_player = switch_player(current_player)

        except ValueError:
            print("Possible values: '1', '2' or '3'.")
        except TooManyPencilsTaken:
            print("Too many pencils were taken.")
    return current_player


def determine_the_winner(player, bot, current_player):
    winner = player if current_player == player else bot
    print(f"{winner} won!")


if __name__ == "__main__":
    player = "John"
    bot = "Bender"

    pencils = ask_number_of_pencils()
    current_player = determine_first_player()
    current_player = play_game(pencils, current_player)
    determine_the_winner(player, bot, current_player)
