#!/usr/bin/env python

######################################################################
# @author      : nevernew (nevernew@orca)
# @file        : 8_exercise_2
# @created     : Четверг ноя 15, 2018 13:06:46 MSK
#
# @description : Задание два 
######################################################################

class User():
    count = 0
    def __init__(self, name, login, pas):
        self._name = name
        self._login = login
        self._pas = pas
        self.count += 1

    def get_name(self):
        print(self._name)

    def set_name(self, ddd):
        print("Acces Denied")

    name = property(get_name,set_name)

    def show_info(self):
        print(self._name, self._login)

class SuperUser(User):
    def __init__(self,name,login,pas,mod):
        super().__init__(name,login,pas)
        self._mod = mod
    
user1 = User('Pasha Match', 'pash','1234')
user1.name
user1.name = 'asdfasd'

admin1 = SuperUser('Arsen', 'arra','1234',"0001")
admin1.show_info()
print(admin1.count)
