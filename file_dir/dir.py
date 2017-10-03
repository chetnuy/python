#!/bin/python

import os

files = os.listdir(path="/home/nevernew/zim/man")
images = filter(lambda x: x.endswith('.txt'), files)
i=0
for d in images:
    i=i+1
    print(str(i)+' '+d)

