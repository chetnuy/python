#!/usr/bin/env python

######################################################################
# @author      : ash (ash@me)
# @file        : 6_example
# @created     : Вторник ноя 13, 2018 20:48:50 MSK
#
# @description : Контрольное задание 
######################################################################


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def move_to(self,x,y):
        self._x = x
        self._y = y

    def move_by(self,x,y):
        self._x +=x
        self._y +=y

    @property 
    def x(self):
        return self._x

    @x.setter
    def x(self,x):
       self._x = x

    @property 
    def y(self):
        return self._y

    @y.setter
    def y(self,y):
        self._y = y 

    def __repr__(self):
        return "I am"


    




point = Point(10,20)

print(point.x)
point.x = 12
print(point.x)
print(point.y)
point.y = 13
print(point.y)

point.move_by(10,20)
print(point.y)
print(point.x)

point.move_to(1,2)
print(point.y)
print(point.x)
print(point)
