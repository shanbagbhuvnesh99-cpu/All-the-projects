import random

def number_guessing_game():
    print("Welcome To The Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess a number (1–100): "))

            if guess < 1 or guess > 100:
                print("Number must be between 1 and 100.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print(f"Too low! Attempts left: {max_attempts - attempts}")
            elif guess > number_to_guess:
                print(f"Too high! Attempts left: {max_attempts - attempts}")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Enter numbers only.")

    else:
        print(f"Game Over! The number was {number_to_guess}.")

number_guessing_game()
