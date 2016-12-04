import MySQLdb # импортируем модуль
#con = MySQLdb.connect(host='localhost', user='root', password='sad1') #подключаемся к серверу
con = MySQLdb.connect(host='localhost', user='root', password='sad1', db='python') #подключаемся к серверу
#f =con.get_character_set_info() #смотрим настройки кодировки
#con.set_character_set('uft-8') # устанавливаем кодировку

# #выполняем простые запросы к базе данных
# cur = con.cursor() # Создаем объект-курсор
# sql = """DROP DATABASE data"""
# try:
# # Обрабатываем исключения
#     cur.execute(sql)
# # Выполняем SQL-запрос
# except MySQLdb.DatabaseError as err:
#     print (u"Ошибка:", err)
# else:
#     print (u"Запрос успешно выполнен")
# cur.close()
# # Закрываем объект-курсор
# con.close()
# input()

'''
cur = con.cursor()
# Создаем объект-курсор
sql = """CREATE DATABASE `python`
DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci"""
try:
# Обрабатываем исключения
    cur.execute(sql)
# Выполняем SQL-запрос
except MySQLdb.DatabaseError as err:
    print (u"Ошибка:", err)
else:
    print (u"Запрос успешно выполнен")
cur.close()
# Закрываем объект-курсор
con.close()
input()
'''

# заполняем таблицу
# cur = con.cursor()
# sql_1 = """\
# CREATE TABLE `city` (
# `id_city` INT NOT NULL AUTO_INCREMENT,
# `name_city` CHAR(255) NOT NULL,
# PRIMARY KEY (`id_city`)
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8"""
# sql_2 = "INSERT INTO `city` VALUES (NULL, 'Санкт-Петербург')"
# try:
#     cur.execute("SET NAMES utf8") # Кодировка соединения
#     cur.execute(sql_1)
#     cur.execute(sql_2)
# except MySQLdb.DatabaseError as err:
#     print (u"Ошибка:", err)
# else:
#     print (u"Запрос успешно выполнен")
# con.commit()
# cur.close()
# con.close()
# input()
'''
con.autocommit(True) # Автоматическое завершение транзакции
cur = con.cursor()
t1 = ("Москва",) # Запятая в конце обязательна!
t2 = (3, "Новгород")
d = {"id": 4, "name": """Новый ' " город"""}
sql_t1 = "INSERT INTO `city` (`name_city`) VALUES (%s)"
sql_t2 = "INSERT INTO `city` VALUES (%s, %s)"
sql_d = "INSERT INTO `city` VALUES (%(id)s, %(name)s)"
try:
    cur.execute("SET NAMES utf8") # Кодировка соединения
    cur.execute(sql_t1, t1)
# Кортеж из 1-го элемента
    cur.execute(sql_t2, t2)
# Кортеж из 2-х элементов
    cur.execute(sql_d, d)
# Словарь
except MySQLdb.DatabaseError as err:
    print (u"Ошибка:", err)
else:
    print (u"Запрос успешно выполнен")
cur.close()
con.close()
input()
'''

'''
# используем метод executemany()

# -*- coding: utf-8 -*-
con.autocommit(True) # Автоматическое завершение транзакции
cur = con.cursor()
arr = [ ("Пермь",), ("Самара",) ]
sql = "INSERT INTO `city` (`name_city`) VALUES (%s)"
try:
    cur.execute("SET NAMES utf8") # Кодировка соединения
    cur.executemany(sql, arr)
# Выполняем запрос
except MySQLdb.DatabaseError as err:
    print (u"Ошибка:", err)
else:
    print (u"Запрос успешно выполнен")
cur.close()
con.close()
input()
'''

# # выводим содержимое таблицы через цикл
# con.autocommit(True)
# cur = con.cursor()
# cur.execute("SELECT * FROM `city`")
#
# for row in cur: print(row)


# Теперь используем библиотеку PyODBC
# подключаем библиотеки для компиляции pip установки
# ставим unixodbc - для комплятора
# myodbc - для подключения драйвера, название можно посмотреть /etc/unixodbc/odbc.ini
'''
import pyodbc
s = "DRIVER={myodbc-5.2};SERVER=localhost;"
s += "UID=root;PWD=sad1;DATABASE=python"
con = pyodbc.connect(s, autocommit=True, unicode_results=True)
cur = con.cursor()
sql_1 = """\
CREATE TABLE `user` (
`id_user` INT AUTO_INCREMENT PRIMARY KEY,
`email` VARCHAR(255),
`passw` VARCHAR(255)
) ENGINE = MYISAM CHARACTER SET utf8 COLLATE utf8_general_ci
"""
sql_2 = """\
CREATE TABLE `rubr` (
`id_rubr` INT AUTO_INCREMENT PRIMARY KEY,
`name_rubr` VARCHAR(255)
) ENGINE = MYISAM CHARACTER SET utf8 COLLATE utf8_general_ci
"""
sql_3 = """\
CREATE TABLE `site` (
`id_site` INT AUTO_INCREMENT PRIMARY KEY,
`id_user` INT,
`id_rubr` INT,
`url` VARCHAR(255),
`title` VARCHAR(255),
`msg` TEXT,
`iq` INT
) ENGINE = MYISAM CHARACTER SET utf8 COLLATE utf8_general_ci
"""
try:
    cur.execute(sql_1)
    cur.execute(sql_2)
    cur.execute(sql_3)
except pyodbc.Error as err:
    print (u"Ошибка:", err)
else:
    print (u"Запрос успешно выполнен")
cur.close()
con.close()
input()
'''

# import pyodbc
# s = "DRIVER={myodbc-5.2};SERVER=localhost;"
# s += "UID=root;PWD=sad1;DATABASE=python"
# con = pyodbc.connect(s, autocommit=True, unicode_results=True)
# cur = con.cursor()
# sql_1 = "INSERT INTO `user` (`email`, `passw`) VALUES (?, ?)"
# sql_2 = "INSERT INTO `rubr` (`name_rubr`) VALUES (?)"
# sql_3 = "INSERT INTO `rubr` VALUES (NULL, ?)"
# try:
#     cur.execute(sql_1, ('unicross@mail.ru', 'password1'))
#     cur.execute(sql_2, ("Программирование",))
#     cur.execute(sql_3, """Поисковые ' " порталы""")
# except pyodbc.Error as err:
#     print (u"Ошибка:", err)
# else:
#     print (u"Запрос успешно выполнен")
# cur.close()
# con.close()
# input()

import pyodbc
# используем executemany
s = "DRIVER={myodbc-5.2};SERVER=localhost;"
s += "UID=root;PWD=sad1;DATABASE=python"
con = pyodbc.connect(s, autocommit=True, unicode_results=True)
cur = con.cursor()
arr = [
(1, 1, "http://wwwadmin.ru", "Название", "", 100),
(1, 1, "http://python.org", "Python", "", 1000),
(1, 2, "http://google.ru", "Гугль", "", 3000)
]
sql = """INSERT INTO `site` \
(`id_user`, `id_rubr`, `url`, `title`, `msg`, `iq`) \
VALUES (?, ?, ?, ?, ?, ?)"""
try:
   cur.executemany(sql, arr)
except pyodbc.Error as err:
   print (u"Ошибка:", err)
else:
   print (u"Запрос успешно выполнен")
cur.close()
con.close()
input()