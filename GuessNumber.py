import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x} :"))

        if guess < random_number:
            print("Sorry...Guess again... too low")
        elif guess > random_number:
            print("Sorry...Guess again...too high")

    print(f"Yay....You have guess the number {guess} correctly")


guess(100)