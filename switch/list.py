#!/usr/bin/env python3

#Create a list
#Have a menu add, remove number of items
#Print the list after each operation
#TODO - Implement a switch statement with a dictionary calling a function

import pdb
import os
import sys
os.system('clear')

mylist = [1,2,3,4,5,6]

def menu():
    print('\n')
    print('1 - Print list')
    print('2 - Insert at position')
    print('3 - Append to the list')
    print('4 - Print the size of the list')
    print('0 - Exit')
    
    option = int(input('Enter your choice: '))
    print('\n')
    return option

#Menu Functions
def plist():
    print(mylist)

#def ins():

#def app():

#def size():

def exit():
    sys.exit()

#Create Dictionary
def switch(choice):
    choices = {
    0: exit,
    1: plist,
    }
    # Get the function from switcher dictionary
    func = choices.get(choice, lambda: "Invalid month")
    # Execute the function
    func()

while(True):
    c = menu()
    switch(c)
