#!/usr/bin/env python

# @author      : ash (ash@wave)
# @created     : Воскресенье ноя 25, 2018 19:24:53 MSK
# @description :  simply thread

import threading

def watch(num):
    print("Thread: ",num)


for i in range(9):
    threading.Thread(target=watch, args=[i]).start()


