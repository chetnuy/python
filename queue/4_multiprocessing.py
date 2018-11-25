#!/usr/bin/env python

# @author      : ash (ash@wave)
# @created     : Воскресенье ноя 25, 2018 19:13:31 MSK
# @description : for multiproccessing queue


from multiprocessing import Queue


q = Queue()

q.put('one')
q.put('two')
q.put('three')
q.put('four')

print(q.get())
q.put('new three')
print(q.get())
