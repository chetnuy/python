#!/usr/bin/env python

######################################################################
# @author      : nevernew (nevernew@orca)
# @file        : 9_design
# @created     : Четверг ноя 15, 2018 13:38:33 MSK
#
# @description : Дизайн ООП
######################################################################

"""
Solid принципы
Single - каждый инструмент для своей задачи
Open/close - отрыты для расширения, но закрыты для модификации
 
"""

import abc

class AbstractPoint(abc.ABC):
    @abc.abstractclassmethod
    def setup(self):
        pass

class Point(AbstractPoint):
    def setup(self):
        return 0

point = Point()
