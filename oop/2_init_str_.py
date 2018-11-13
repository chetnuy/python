#!/usr/bin/env python

class First:
    #конструктор
    #используем self - так как первым аргументом всегда передается имя вызвавшего класса
    def __init__ (self, var):
        # declarate private variblies
        self._var = var
        # make private variables
        self.__var = var


    def fire(self):
        print("Fire"*self.__var)
    def __str__(self):
        #стринг для человека, репр для возможной сериализации
        return "String info"
    def __repr__(self):
        return "Reprisintation info"

first = First(23)
fire = first.fire()

#Узнаем что за класс
print(type(first))

#Принадлежит ли экзeмпляр данному классу
print(isinstance(first,First))
print(first)

print(first._var)
#print(first.__var)



