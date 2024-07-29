import random

def play_guessing_game():
    """🤓 Plays a number guessing game with the user.

    The user has two tries to guess a secret number between 1 and 5.
    Provides feedback on whether the guess is too high or too low.
    """
    print("\nWelcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 5. You have 2 guesses to find it.")

    secret_number = random.randint(1, 5)
    guesses_left = 2

    while guesses_left > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 5.")
            continue

        if not 1 <= guess <= 5:
            print("🙅 Out of bounds! Guess must be between 1 and 5.")
            continue

        guesses_left -= 1

        if guess == secret_number:
            print("🎉 Congratulations! You guessed it!")
            break
        elif guess < secret_number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

        if guesses_left > 0:
            print(f"You have {guesses_left} guess left.")
        else:
            print(f"😔 Sorry, you're out of guesses. The number was {secret_number}.")


# Start the game directly when the script is run
if __name__ == "__main__":
    play_guessing_game()
