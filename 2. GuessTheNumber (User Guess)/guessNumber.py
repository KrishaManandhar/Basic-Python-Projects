# GUESS THE NUMBER (Guessing number by user)
import random

def guessNumber(x):
    random_number = random.randint(1,x)
    guess = 0
    while(guess!=random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess<random_number:
            print("Try again! It's too low")
        elif guess>random_number:
            print("Try again! It's too high")
    print(f"Hurrey! congrats. You got it correct guess number {random_number}")

guessNumber(10)
