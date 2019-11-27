#!/usr/bin/env python3

#Create a list
#Have a menu add, remove number of items
#Print the list after each operation

import pdb
import os
os.system('clear')

mylist = []

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
    
while(True):
    option = menu()

    #Print the list
    if option == 1:
        if len(mylist) == 0:
            print('The list is empty.')
        else:
            print(mylist)

    #Insert at position
    if option == 2:
        insertat = int(input('Enter position to insert from 0 to {} : '.format(len(mylist)))
        item = input('Enter a new list item to insert at the given position: ')

        #Add numeric check
        mylist.insert(insertat, item)

    #Append new item to the end of the list
    if option == 3:
        item = input('Enter a new list item: ')
        if item.isnumeric() == False:
            mylist.append(item)
        elif item.isnumeric() == True:
             mylist.append(int(item))

    #Print the number of items in the list
    if option == 4:
        print('The number of items in the list is: ', len(mylist))

    #Exit
    if option == 0:
        print('Exiting...')
        break

