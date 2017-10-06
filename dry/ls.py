#!/bin/python
# -*- coding: utf-8 -*-
#
# author: alex pokrov
# date: 10/3/17 time: 7:26 PM
# simple diary
# first step create base_file!!!

import uuid
import os
import datetime
import argparse

def read_write():

    #Устанавливаем базу
    base_file = "/mnt/python/dry/base.txt"

    #получаем дату
    now = datetime.datetime.now()
    data_dry = now.strftime("%Y-%m-%d")


    # создаем темп файл и открываем его в vim
    tmpfile = '/tmp/' + str(uuid.uuid4()) + '.txt'
    os.system('vim %s' % tmpfile)

    #записываем в конец нашей базы
    with open(tmpfile, 'r') as fin1:
        lines = fin1.readlines()
    with open(base_file, 'a+') as fout:
        fout.write(data_dry+' ==='+'\n'+''.join(list(lines)))

    #закрываем файл и удаляем tmp
    fin1.closed
    os.remove(tmpfile)

    #Проверка на повторяющуюся дату
    def remove_data(filename, string):

        tempname = filename + '.temp' # os.tempnam() gives warning

        with open(filename) as fin:
            x=0 # python 2.6
            with open(tempname, 'w') as fout:   # compatible
                for line in fin:
                    line = line.rstrip('\n');
                    if line != string+' ===':
                        fout.write(line+'\n')
                    elif line == string+' ===' and x==0:
                        fout.write(line +'\n')
                        x+=1

        os.rename(tempname, filename)
    remove_data(base_file, data_dry)
parser = argparse.ArgumentParser(description='Anda - Simple diary for live')
# The -- indicates that it is optional
parser.add_argument('-v', '--verbose', help='verbose about programm', action='store_true')
args = parser.parse_args()
if args.verbose:
    read_write()
else:
    read_write()



