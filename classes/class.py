#!/usr/bin/env python3

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

name = input('Enter your name: ')
score = input('Enter your score: ')

p1 = Player(name, score)

print(p1.name)
print(p1.score)
