import random

def guessing_game():
    secret = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number (1-10): "))

        if guess == secret:
            print("Correct Guess!")
            break
        elif guess < secret:
            print("Too Low!")
        else:
            print("Too High!")

guessing_game()