#!/usr/bin/env python

######################################################################
# @author      : nevernew (nevernew@orca)
# @file        : deque
# @created     : Среда ноя 21, 2018 23:15:47 MSK
#
# @description :    Двухконечная очередь 
######################################################################

from collections import deque

q = deque()

q.append("one")
q.append("two")
q.append("three")
q.append("four")

print(q)

#Возращает последний элемент lifo
print(q.pop())
#Возвращает первый
print(q.popleft())
print(q.popleft())
print(q.popleft())
#error
#print(q.popleft())

