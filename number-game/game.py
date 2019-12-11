#!/usr/bin/env python3

#Generate a Random Number
#Have the user guess numbers until its right
#Say higher or lower
#Keep track of nymber of trys
#TODO Store player scores in a file 


import random
import sys

numrange = int(sys.argv[1])

number = random.randint(1,numrange)
attempts = 1

print('The random number is in the range from 1 to', numrange)

while (True):
    guess = int(input('Enter your guess: '))
    attempts = attempts + 1
    if guess < number:
        print('Your guess is smaller.')
    elif guess > number:
        print('Your guess is bigger.')
    else: 
        break
print('You are correct.')
print('You guessed in', attempts, 'attempts.')




