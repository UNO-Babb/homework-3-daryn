#Example Flask App for a hexaganal tile game
#Logic is in this python file

import random

def choose_word():
    words = ['snakes', 'games', 'computer', 'winows', 'kansas' , 'dog' , 'lady' , 'girls' , 'starbucks' , 'cupcake' , 'ladder' , 'chair' , 'batman', 'grass']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    guessed = ["_"] * len(word)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("Word: " + " ".join(guessed))

    while tries > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("Wrong guess!")
            tries -= 1

        print(display_hangman(tries))
        print("Word: " + " ".join(guessed))

    if "_" not in guessed:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Game over! The word was:", word)

def main():
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

main()

play_hangman()
