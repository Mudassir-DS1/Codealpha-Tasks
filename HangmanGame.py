import random


def select_random_word():
    words = ['python', 'hangman', 'programming', 'data', 'science']
    return random.choice(words)


def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(display_word(word, guessed_letters))
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've guessed the word correctly.")
                break
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
            print(display_word(word, guessed_letters))

        if incorrect_guesses == max_incorrect_guesses:
            print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
    hangman()
