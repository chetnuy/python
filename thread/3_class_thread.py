#!/usr/bin/env python

# @author      : nevernew (nevernew@mail.ru)
# @created     : 28/11/2018
# @description : simply class

import threading
import datetime

class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def print_date(self, threadName, counter):
        datefields = []
        today = datetime.date.today()
        datefields.append(today)
        print ("%s[%d]: %s" % ( threadName, counter, datefields[0] ))

    def run(self):
        print ("Запуск " + self.name)
        self.print_date(self.name, self.counter)
        print ("Выход " + self.name)


# Создание новой нити
thread1 = myThread("Нить", 1)
thread2 = myThread("Нить", 2)

# Запуск новой нити
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print ("Выход из программы!!!")
