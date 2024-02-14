# 1. The user inputs their name to initiate the game.
def welcome():
    print("Enter your name:")
    name = input()
    print("-------------")

    # 2. The program communicates the game rules and instructs the user to guess the randomly chosen word.
    print("Welcome " + name + " to the Word Guessing Game!")
    print("Try to guess the word.")
    print("You will be given 12 attempts to find the word")
    print("For each letter in your guess:")
    print(
        "- If the letter is in the correct position, it will be marked in \033[92mgreen\033[0m."
    )
    print(
        "- If the letter is in the word but in the wrong position, it will be marked in \033[93myellow\033[0m."
    )
