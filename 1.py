
#!/usr/bin/python
# !_*_coding: utf-8 -*-
# print('hello')
# print('привет')
#
# for i  in range (1, 11): print(i)
"""
ghbdsfasdfasdf
"""
# print(""" ddd dd
# dasdfasd
# asdfasd
#
# """)
#простой ввод через input
# try:
#     name = input('введите свое имя: ')
#     print('ваше имя '+ name)
# except EOFError:
#     print('обработка ошибки')
#raw_input input - теперь равнозначны

#обработка аргументов
"""
простой вывод аргументов введенных с помощью параметров
import sys
arr = sys.argv[:]
for i in arr:
    print(i)
"""
"""
r = input('введите число')
arr = int(r)
if arr == 0:

    print('null')
elif arr==1:
    print('one')
else:
    print('other input')
print(arr)
"""
"""
mas = [(1,2), (2,4)]

for a,b in mas:
    print(a)
    print(b)
"""

# b = 0; sum=0
# while True:
#     a = input('input numeric for exit input "stop"')
#     if a == 'stop':
#        break;
#     else:
#        b = int(a)
#        sum +=b
#        print(sum)
# print("end goal ",sum)
"""
import math
a = math.sqrt(25)
print(a)
"""
"""
import random
print(random.randint(0,100))
"""
# s = str("dd","utf-8")
# print(s)
'''#простое инвертирование сроки
s = "hello"
print(s[::-1])
'''
"""
#Простая шифровка пароля
import hashlib
PSword = input('Input password  ') # вводим пароль
bytecode = PSword.encode() # кодируем в байты
h = hashlib.md5(bytecode) #cнимаем хэш сумму

savepass = '5f4dcc3b5aa765d61d8327deb882cf99'
print(h.hexdigest())
hh =h.hexdigest()
if h.hexdigest()== savepass: #сравниваем строку хэша с нашим паролем
    print('true true', )
    print(type(hh))
"""
"""
#пароль с солью и количеством проходов
import hashlib
PSword = input('Input password  ') # вводим пароль
bytecode = PSword.encode() # кодируем в байты
h = hashlib.pbkdf2_hmac('md5',bytecode, b"sasdfsd",1000) #cнимаем хэш сумму

savepass = b'\xcc&r9\xc6;g\x0cl\x00\x84:d^\xa2h'
print(h)

if h == savepass: #сравниваем строку хэша с нашим паролем
    print('true true', )
"""

# d = dict(a=1,b=2)
# print(d)
""""
#Объединение двух списков
name = ['l','k']
nume = [1,2]
d = list(zip(name,nume))
print(d)
"""

'''
d ={'d':1, 'b':2}
print(d)
d.update(c=3)
print(d)
'''
'''
#plain output date and time
import time
print(time.strftime('%c'))
'''
'''
#Простой календарик по заданной дате
import calendar
c = calendar.LocaleTextCalendar()
print(c.formatmonth(2016,2))
'''

# #вывести календарь за указанный год
# import calendar
# print(calendar.calendar(2016))
'''
#измерение времени выполнения кода
from timeit import Timer
code= """\
i, j = 1,0
while i< 1000:
    i+=1

"""
t1=Timer(stmt=code)
print(t1.timeit(number=10000))
'''
'''
#простейшая функция
def sum(x):
    return print(x)
f =sum('Да здравствует революция')
print(sum('hello'))
'''
'''
def fun1(f):
    print("hello")
    return f
def fun2(x):
    print("heloo2")
    return(x)
@fun1
@fun2
def fun3():
    return(print('fun3'))
print(fun3())
'''

class Myclass:
    def __init__(self):
        self.x = 10
    def print_x(self):
        print(self.x)
c = Myclass()
c.print_x()
print(c.x)


