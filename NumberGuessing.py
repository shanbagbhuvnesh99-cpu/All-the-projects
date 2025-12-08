# Number Guessing Game with Hints

import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 1000.")
    print("Try to guess it in as few attempts as possible!\n")

    number_to_guess = random.randint(1, 1000)
    attempts = 0
    max_attempts = 100
    guessed = False
    previous_guesses = []

    while attempts < max_attempts and not guessed:
        try:
            guessed_number = int(input("Make a guess: "))
            attempts += 1
            previous_guesses.append(guessed_number)

            if guessed_number < 1 or guessed_number > 1000:
                print("⚠️ Please guess a number between 1 and 1000.")
                continue

            if guessed_number < number_to_guess:
                print("Too low.")
            elif guessed_number > number_to_guess:
                print("Too high.")
            else:
                guessed = True
                print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
                break

            # 🔍 Add hint system
            difference = abs(number_to_guess - guessed_number)
            if difference <= 5:
                print("🔥 Very hot! You’re super close!")
            elif difference <= 15:
                print("🌡️ Hot! You’re close.")
            elif difference <= 50:
                print("🙂 Warm... keep trying.")
            else:
                print("❄️ Cold... try a different range.")

        except ValueError:
            print("🚫 Invalid input. Please enter a number between 1 and 1000.")

    if not guessed:
        print(f"\n😢 Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
        print("Your previous guesses were:", previous_guesses)


# Run the game
number_guessing_game()
