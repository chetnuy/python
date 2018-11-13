#!/usr/bin/env python

######################################################################
# @author      : ash (ash@me)
# @file        : decorator
# @created     : Вторник ноя 13, 2018 14:57:22 MSK
#
# @description : используем декоратор для инкапсуляции 
######################################################################


class Example: 
    def __init__(self):
        self.__private = "blabla"
    #getter
    @property 
    def private(self):
        return self.__private

    #setter 
    @private.setter 
    def private(self,value):
        self.__private = value

example = Example()

print(example.private)
example.private = "blsa"
print(example.private)
