#!/usr/bin/env python

# @author      : ash (ash@wave)
# @created     : Воскресенье ноя 25, 2018 18:48:39 MSK
# @description : list for simply queue
'''
queue is fifo
stack for lifo
'''

list = []

list.append("one")
list.append("two")
list.append("three")
list.append("four")


print(list.pop(0)) #one
list.append("five") 
print(list.pop(0)) #two



