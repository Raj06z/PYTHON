import random
secret_number = random.randint(1, 20)
attempts = 0

print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 20.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
