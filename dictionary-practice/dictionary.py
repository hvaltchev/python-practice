#!/usr/bin/env python3

#Create a list
#Have a menu add, remove number of items
#Print the list after each operation

import pdb
import os
os.system('clear')

dictionary = {}

def menu():
    print('\n')
    print('1 - Print dictionary')
    print('2 - Insert key value pair')
    print('3 - Delete key value pair')
    print('4 - Print the size of the dictionary')
    print('0 - Exit')
    
    option = int(input('Enter your choice: '))
    print('\n')
    return option
    
while(True):
    option = menu()

    #Print the dictionary
    if option == 1:
        print(dictionary)

    #Insert key value pair
    if option == 2:
        key = input('Enter a key: ')
        value = input('Enter a value: ')

        dictionary[key] = value 

    #Delete key value pair
    if option == 3:
        key = input('Enter a key that you want to delete by: ')
        del dictionary[key]

    #Print the size of the dictionary
    if option == 4:
        size = len(dictionary)
        print('The size of the dictionary is', size)

    if option == 0:
        break
