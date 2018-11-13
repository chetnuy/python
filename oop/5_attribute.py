#!/usr/bin/env python

######################################################################
# @author      : ash (ash@me)
# @file        : 5_attribute
# @created     : Вторник ноя 13, 2018 15:13:50 MSK
#
# @description : атрибуты в классе и атрибуты в экземпляре класса 
######################################################################

class Parrent:
    couter = 0
    name = "Blash"
    def __init__(self, value):
        self.couter = value



parrent = Parrent(10)

print(parrent.couter)
print(parrent.name)
print(Parrent.couter)
