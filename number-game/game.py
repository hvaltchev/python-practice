#!/usr/bin/env python3

#Generate a Random Number
#Have the user guess numbers until its right
#Say higher or lower
#Keep track of nymber of trys

import random

number = random.randint(1,100)

while (True):
    guess = int(input('Enter your guess: '))
    if guess < number:
        print('Your guess is smaller.')
    elif guess > number:
        print('Your guess is bigger.')
    elif guess == number:
        break
print('You are correct.')
