# Steps
# 1. The user inputs their name to initiate the game.
# 2. The program communicates the game rules and instructs the user to guess the randomly chosen word.
# 3. The user guesses a WORD.
# 4. For each letter in the guessed word:
#    - If the letter is in the correct position, it will be marked in green.
#    - If the letter is in the word but in the wrong position, it will be marked in yellow.
#    - If the letter is not in the word at all, it will be marked in red.
# 5. The program displays the feedback for the guessed alphabet using green, yellow, and red indicators.
# 6. The program keeps track of the number of turns and deducts one turn after each guess.
# 7. Steps 3 to 6 are repeated until the user correctly guesses the entire word or exhausts the maximum number of turns (e.g., 12 turns).
# 8. The game outcome is determined:
#    - If the user correctly guesses the entire word within the allowed turns, they win.
#    - If the user runs out of turns without guessing the complete word, they lose.
# 9. The program asks if the user wants to play again. If yes, return to step 2; if not, end the game.


# 1. The user inputs their name to initiate the game.
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
