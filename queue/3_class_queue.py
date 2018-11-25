#!/usr/bin/env python

# @author      : ash (ash@wave)
# @created     : Воскресенье ноя 25, 2018 19:00:20 MSK
# @description : class queue


'''
queue.Queue
Синхронизированная очередь.
Может подойти для нескольких процессов
'''


from queue import Queue

q = Queue()

q.put('eat')
q.put('sleep')
q.put('cross')
q.put('simply')

print(q)

print(q.get())
print(q.get())
q.put('new cross')
print(q.get())
print(q.get())
print(q.get())
