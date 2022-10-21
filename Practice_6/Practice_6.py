"""

    Generate a random integer from a to b. You and your friend have to guess a number between two
    numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will
    have to keep choosing the number and your progam must tell whether the number is greater than the
    actual number or less than the actual number. Log the number of trials it took your friend to arrive at the
    number. You play the same game and then the person with minimum number of trials wins!

    Randomly generate a number and don't show that to the user

"""

import random

no_of_player = 2


def main():
    try:
        take_input()
    except Exception as e:
        print(e)


def take_input():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    random_num = random.randint(a, b)
    print(random_num)
    action = str(input("Are you ready to start the game? (y/N)"))
    if action.lower() == "y":
        scores = dict(game_start(random_num))
        reversed_scores = {v: k for k, v in scores.items()}
        max_score = min(reversed_scores.keys())
        winner = reversed_scores.get(max_score)
        print(f"The winner is Player {winner}")
    else:
        print("It seems you are not interested to play.")


def game_start(random_num):
    scores = {}
    for i in range(no_of_player):
        tries = 0
        while True:
            a = int(input(f"Player {i + 1} - Guess the number: "))
            if a == random_num:
                print(f"Number guessed in {tries + 1} tries.")
                scores[i + 1] = tries + 1
                break
            tries += 1
    return scores


if __name__ == "__main__":
    main()
