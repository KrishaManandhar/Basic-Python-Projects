# GUESS THE NUMBER (guessing number by computer)
import random

def guess_by_computer(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low!=high :
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too high(H), too low (L), or correct(C)')
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f"Hurrey! The computer guessed the number, {guess} correctly")

guess_by_computer(10)