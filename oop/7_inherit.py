#!/usr/bin/env python

######################################################################
# @author      : ash (ash@me)
# @file        : 7_inherit
# @created     : Среда ноя 14, 2018 14:09:56 MSK
#
# @description : Наследование и переопределение методов 
######################################################################


class Point(object):
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def mode_to(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Я класс Point {} {}'.format(self._x, self._y)




class Point3D(Point):

    def __init__(self,x,y,z):
        self._z = z 
        super().__init__(x,y)

    def __repr__(self):
        s = super().__repr__()
        return s+" Переопределечн"


point3d = Point3D(3,4,5)
print(point3d)


