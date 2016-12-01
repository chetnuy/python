#!/usr/bin/python

import random
sum = ""
size = input("input lange password (or default lange = 8) ")

if size == "": # определяем количество символов
    s=8
else: s=int(size)
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m',

'n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L',
'M','N','O','P','Q','R','S','T','U','V', 'W',
'X','Y','Z','1','2','3','4','5','6','7','8','9','0'] # массив с символами

for i in range(s):
    sum+=random.choice(arr)
print(sum)

