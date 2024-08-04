import random
def guess_the_number():
    print("Guess the Number Game")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = input("Guess a number between 1 and 100 or 'q' to quit: ")

        if user_guess.lower() == 'q':
            print(f"Okay, the number was {number_to_guess}.")
            break

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if user_guess < 1 or user_guess > 100:
            print(" Guess a number between 1 and 100.")
            continue

        attempts += 1

        if user_guess == number_to_guess:
            print(f"Congratulations! You found the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

if __name__ == "__main__":
    guess_the_number()