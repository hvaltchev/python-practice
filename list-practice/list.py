#!/usr/bin/env python3

#Create a list
#Have a menu add, remove number of items
#Print the list after each operation

import os
os.system('clear')

mylist = [1, 2, 3]

def menu():
    print('1 - Print list')
    print('2 - Append to the list')
    print('3 - Print the size of the list')
    print('0 - Exit')
    
    option = int(input('Enter your choice: '))
    print('\n')
    return option

    
while(True):
    option = menu()

    #Print the list
    if option == 1:
        print(mylist)
    
    #Append new item to the end of the list
    if option == 2:
        item = input('Enter a new list item: ')
        if item.isnumeric() == False:
            mylist.append(item)
        elif item.isnumeric() == True:
             mylist.append(int(item))

    #Print the number of items in the list
    if option == 3:
        print('The number of items in the list is: ', len(mylist))

    #Exit
    if option == 0:
        print('Exiting...')
        break

