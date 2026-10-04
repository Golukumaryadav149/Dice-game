import random
from utils import show_result


def roll_dice():

    return random.randint(1, 6)



def play_game():

    print("\n--- New Game Started ---")
    player = input(" give me player name :")

    player = roll_dice()

    computer = roll_dice()


    print("player rolled:", player)

    print("Computer rolled:", computer)


    show_result(player, computer)