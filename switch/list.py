#!/usr/bin/env python3

import pdb
import os
import sys
os.system('clear')

mylist = [1,2,3,4,5,6]

def menu():
    print('\n')
    print(' 1 - Print list')
    print(' 2 - Append to the list')
    print(' 3 - Extend')
    print(' 4 - Insert at position')
    print(' 5 - Remove')
    print(' 6 - Pop')
    print(' 7 - Clear')
    print(' 8 - Index')
    print(' 9 - Print the size of the list')
    print('10 - Sort the list')
    print('11 - Reverse the list')
    print('12 - Copy')
    print(' 0 - Exit')
    
    option = int(input('Enter your choice: '))
    print('\n')
    return option

#Menu Functions
def plist():
    print(mylist)

def app():
    item = input('Enter a new list item: ')
    if item.isnumeric() == False:
        mylist.append(item)
    elif item.isnumeric() == True:
        mylist.append(int(item))

def extend():
    x = list(map(int, input("Enter a multiple values to extend the list with: ").split())) 
    mylist.extend(x)

def ins():
    insertat = int(input('Enter position to insert from 0 to {} : ' .format(len(mylist))))
    item = input('Enter a new list item to insert at the given position: ')
    mylist.insert(insertat,item)

def remove():
    item = int(input('Enter a value to remove from the list: '))
    mylist.remove(item)


def pop():
    mylist.pop()

def clear():
    mylist.clear()

def index():
    item = int(input('Enter an index from 0 to {} : ' .format(len(mylist))))
    print('The item at the inedex is : ', mylist.index(item))

def size():
    print('The size of the list is',len(mylist))

def sort():
    mylist.sort()

def reverse():
    mylist.reverse()

def copy():
    copy = mylist.copy()
    print(copy)

def exit():
    sys.exit()

#Create Dictionary
def switch(choice):
    choices = {
    0: exit,
    1: plist,
    2: app,
    3: extend,
    4: ins,
    5: remove,
    6: pop,
    7: clear,
    8: index,
    9: size,
    10: sort,
    11: reverse,
    12: copy,
    }
   
    # Get the function from switcher dictionary
    func = choices.get(choice, lambda: "Invalid month")
    # Execute the function
    func()

while(True):
    c = menu()
    switch(c)
