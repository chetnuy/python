#!/usr/bin/python

## use get and set method 
## and universal union varibles

class Two:
    def __init__(self):
        self.__private = 10
    
    def get(self):
        return self.__private

    def set(self, value):
        self.__private = value
    """ universal varibles"""
    counter = property(get, set)

two = Two()
print(two.counter)

two.counter = 100
print(two.counter)
