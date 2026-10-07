import random

def play_hangman():
    words = ["apple", "banana", "red", "green", "blue", "yellow", "white", "black"]
    secret_word = random.choice(words)
    displayed_word = ["_"] * len(secret_word)

    attempts_left = 6
    guessed_letters = set()

    print("Welcome to Hangman!")

    while attempts_left > 0 and "_" in displayed_word:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            for index, letter in enumerate(secret_word):
                if guess == letter:
                    displayed_word[index] = guess
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        print(" ".join(displayed_word))

    if "_" not in displayed_word:
        print("Congratulations you win!")
    else:
        print(f"The word was: {secret_word}")

play_hangman()