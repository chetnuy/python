#!/usr/bin/env python

# @author      : ash (ash@wave)
# @created     : Воскресенье ноя 25, 2018 18:54:56 MSK
# @description :  collection.deque

'''
Двухконечная запись (подойдет  для lifo)
Приемлемая скорость

'''

from collections import deque

q = deque()

q.append('one')
q.append('two')
q.append('three')
q.append('four')

print(q)
print(type(q))

print(q.popleft())
q.append('five')
print(q.popleft())
print(q.popleft())
