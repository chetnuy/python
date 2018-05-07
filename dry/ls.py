#!/bin/python
# -*- coding: utf-8 -*-
#
# author: alex pokrov
# date: 10/3/17 time: 7:26 PM

#генирируем случайное имя в
import uuid
import os
import datetime

now = datetime.datetime.now()
data_dry = now.strftime("%Y-%m-%d")


filename = '/tmp/'+ str(uuid.uuid4())+'.txt'


#открываем в виме
os.system('vim %s' % filename)

with open(filename, 'r') as fin1: lines = fin1.readlines()
with open("/mnt/data/python/dry/base.txt", 'a+') as fout: fout.write(data_dry+'\n'+''.join(list(lines)))

#
# f = open("/mnt/data/python/dry/base.txt", 'a+')
# f.write('FUcker\n')
#
#
# d = open(filename, 'r') # выводим содержимое файла
# for line in d:
#     f.write(repr(line))
# f.close()


def remove_string2(filename, string):

    tempname = filename + '.temp' # os.tempnam() gives warning

    with open(filename) as fin:             # python 2.6
        with open(tempname, 'w') as fout:   # compatible
            for line in fin:
                line = line.rstrip('\n');
                if line != string:
                    fout.write(line)
                else

    os.rename(tempname, filename)
remove_string2("/mnt/data/python/dry/base.txt", data_dry)
