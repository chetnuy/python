#!/bin/env python3
# date:    11.11.18
# author:  ash

def Mprint(*args):
 for i in args:
  print(i)


list = ('dd', '11', '333', '4334', '3sdfg')
Mprint(*list)
print(*list,' 1')
