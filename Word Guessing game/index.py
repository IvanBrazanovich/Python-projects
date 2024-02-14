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


# Imports
import random

# I will create the possible words.
from data import wordArray
from helper import welcome

welcome()

### Ways of choosing the random word
list_length: int = len(wordArray)


def game():

    # 3. The user guesses the word
    def pickRandomWord():
        random_number = random.randint(0, list_length - 1)
        return wordArray[random_number]

    randomWord: str = pickRandomWord().lower()

    print("The word has " + str(len(randomWord)) + " letters")
    print("Guess the word")
    print("  ")
    # Check that the length of the guessed word is the same as the random word

    def userGuessWord():
        while True:
            user_try: str = input().lower()
            if len(user_try) != len(randomWord):
                print("The length is not correct, choose again")
            else:
                return user_try

    # Check if it's correct
    def checkCorrect(guessed_word):
        resultData: list = []
        for i in range(0, len(randomWord)):
            # check if the letter is in the same place
            if guessed_word[i] == randomWord[i]:
                resultData.append("\033[92m" + randomWord[i] + "\033[0m")
            elif guessed_word[i] in randomWord:
                resultData.append("\033[93m" + guessed_word[i] + "\033[0m")
            else:
                resultData.append(" ")
        return resultData

    # 12 tries
    for i in range(12):
        guessed_word: str = userGuessWord()
        print(guessed_word + " after guessed")
        if guessed_word == randomWord:
            print("Congratulations. You won!")
            break
        else:
            print("".join(checkCorrect(guessed_word)))
    print(
        "If you want to play again press Y. If you want to finish the game press any other letter"
    )
    userDecision: str = input()
    if userDecision.lower() == "y":
        game()


game()
