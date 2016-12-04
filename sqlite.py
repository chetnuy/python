#!/usr/bin/python
#-*- coding: utf-8 -*-
# import sqlite3 # подключаем модуль
# con = sqlite3.connect('first.db') #открываем бд
# con.close()

#cоздаем базу данных
# import sqlite3
# con = sqlite3.connect("catalog.db")
# cur = con.cursor()
# # Создаем объект-курсор
# sql = """\
# CREATE TABLE user (
# id_user INTEGER PRIMARY KEY AUTOINCREMENT,
# email TEXT,
# passw TEXT
# );
# CREATE TABLE rubr (
# id_rubr INTEGER PRIMARY KEY AUTOINCREMENT,
# name_rubr TEXT
# );
# CREATE TABLE site (
# id_site INTEGER PRIMARY KEY AUTOINCREMENT,
# id_user INTEGER,
# id_rubr INTEGER,
# url TEXT,
# title TEXT,
# msg TEXT,
# iq INTEGER
# );
# """
# try:
# # Обрабатываем исключения
#     cur.executescript(sql) # Выполняем SQL-запросы
# except sqlite3.DatabaseError as err:
#     print('error', err)
# else:
#     print ('ok')
# cur.close()
# # Закрываем объект-курсор
# con.close()
# input()
# # Закрываем соединение

# #заполнить таблицу
#
# import sqlite3
# con = sqlite3.connect("catalog.db")
# cur = con.cursor()
# # Создаем объект-курсор
# sql = """\
# INSERT INTO user (email, passw)
# VALUES ('unicross@mail.ru', 'password1')
# """
# try:
#    cur.execute(sql)
# # Выполняем SQL-запрос
# except sqlite3.DatabaseError as err:
#    print ("Ошибка:", err)
# else:
#    print (u"Запрос успешно выполнен")
#    con.commit()
# # Завершаем транзакцию
# cur.close()
# # Закрываем объект-курсор
# con.close()
# # Закрываем соединение
# input()

#заполнение бд через запросы на картежах
# import sqlite3
# con = sqlite3.connect("catalog.db")
# cur = con.cursor()
# # Создаем объект-курсор
# t1 = (u"Программирование",)
# t2 = (2, u"Музыка")
# d = {"id": 3, "name": u"""Поисковые ' " порталы"""}
# sql_t1 = "INSERT INTO rubr (name_rubr) VALUES (?)"
# sql_t2 = "INSERT INTO rubr VALUES (?, ?)"
# sql_d = "INSERT INTO rubr VALUES (:id, :name)"
# try:
#     cur.execute(sql_t1, t1)
# # Кортеж из 1-го элемента
#     cur.execute(sql_t2, t2)
# # Кортеж из 2-х элементов
#     cur.execute(sql_d, d)
# # Словарь
# except sqlite3.DatabaseError as err:
#     print (u"Ошибка:", err)
# else:
#     print (u"Запрос успешно выполнен")
#     con.commit()
# # Завершаем транзакцию
# cur.close()
# # Закрываем объект-курсор
# con.close()
# # Закрываем соединение
# input()

# создание с помощью метода executesript

# import sqlite3
# con = sqlite3.connect("catalog.db")
# cur = con.cursor()
# # Создаем объект-курсор
# arr = [
# (1, 1, u"http://wwwadmin.ru", u"Название", u"", 100),
# (1, 1, u"http://python.org", u"Python", u"", 1000),
# (1, 3, u"http://google.ru", u"Гугль", u"", 3000)
# ]
# sql = """\
# INSERT INTO site (id_user, id_rubr, url, title, msg, iq)
# VALUES (?, ?, ?, ?, ?, ?)
# """
# try:
#     cur.executemany(sql, arr)
# except sqlite3.DatabaseError as err:
#     print (u"Ошибка:", err)
# else:
#     print (u"Запрос успешно выполнен")
# con.commit()
# # Завершаем транзакцию
# cur.close()
# # Закрываем объект-курсор
# con.close()
# # Закрываем соединение
# input()

'''
import sqlite3
con = sqlite3.connect("catalog.db")
try:
    con.execute("""UPDATE rubr SET name_rubr='Поисковые порталы'
WHERE id_rubr=3""")
except sqlite3.DatabaseError as err:
    print (u"Ошибка:", err)
else:
   con.commit()
# Завершаем транзакцию
   print (u"Запрос успешно выполнен")
con.close()
# Закрываем соединение
input()
'''

# import sqlite3
# con = sqlite3.connect('catalog.db')
# cur = con.cursor()
# #cur.execute("INSERT INTO user (email, passw) VALUES ('admin@site.com', 'suddimudi')")
# #con.commit()
# cur.execute("SELECT * FROM user")
# #print(cur.fetchmany(2)) #выводим указанное количество записей
# #print(cur.fetchall()) #выводим все
# #print(cur.__next__()) #Выводим содержимое запроса каждый раз
#

import MySQLdb
con = MySQLdb.connect(host='localhost', user='root', password='sad1')
f =con.get_character_set_info()
print(f)
