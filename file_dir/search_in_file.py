#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import io

cfiles = input('input folder: ') 
word = input('input word: ') 
with io.open(cfiles, encoding='utf-8') as file:
    for line in file:
        if word in line:
            print(line, end='')
