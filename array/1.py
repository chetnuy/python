#!/bin/python
# -*- coding: utf-8 -*-
#
#       author :     alex pokrov 
#       10/5/17     10:10 PM

arr = [2,3,4,5,4,3,2,3,4,2,3]
x = 0
i = 0
print(arr)
for element in arr:
    if arr[i] == 2 and x == 0:
        x = x+1
    elif arr[i] == 2 and x > 0:
        arr[i]+=1;
    i = i+1

print(arr)
