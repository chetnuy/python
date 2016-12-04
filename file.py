#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
'''
import os,sys
print('%-25s%s' % ('Файл:', os.path.abspath(__file__)))
print('%-25s%s' % ('Текущий каталог:', os.getcwd()))
print('%-25s%s' % ('Путь  файлу:', os.path.abspath('file.txt')))
'''
'''
f = open('file.txt','w+') # открываем и пишем строчку в файл
f.write('my first file \n two line \n')
f.close()
'''
'''
d = open('file.txt', 'r') # выводим содержимое файла
for line in d:
    print(repr(line))
'''

'''
d.write('heoolo')
d.readline()
s.fuck
d.tell()
d.close()

'''
# #запись в файл с помощью операционной системы
# mode = os.O_WRONLY | os.O_TRUNC
# f = os.open('file.txt', mode)
# os.write(f, b'FUcker\n')
# os.close(f)

# чтение файла
# mode = os.O_RDONLY
# f = os.open(r'file.txt', mode)
# os.read(f,50)
# os.close(f)
#
# import os
# os.access('file.txt', os.F_OK)

# #копирование файла
# import shutil
# shutil.copyfile('file.txt', 'filefilefiel')

# позволяет переименовывать файл
# import os
# try:
#     os.rename('filefile', 'new')
# except OSError:
#     print('error string')
# else:
#     print('succeseful')

# удаляем файл
# import os
# try:
#     os.remove('new')
# except OSError:
#     print("file not found")
# else:
#     print('succesefull')


'''
#смотрит атрибуты файла

import os
os.path.getsize('file.txt')
os.path.getatime('file.txt')
f = os.stat('file.txt')
print(f)
'''
'''
#преобразуем относительный путь до файла в абсолютный
import os
f = os.path.abspath('file.txt')
print(f)
'''
'''
# позволяет получить разделить текущую директорию и имя файла
import os
f = os.path.split('/mnt/data2/python/file.txt')
print(f)
'''

'''
#более-менее рабочий код для вывода содержимого файла построчно
import sys
tmp_i = sys.stdin
f = open('file.txt', 'r')
sys.stdin = f
while True:
    try:
        line = input()
        print(line)
    except EOFError:
        print('Error input or output')
        break

sys.stdin = tmp_i
f.close()
input()
'''

'''
# позволяет переключать текущий каталог и выводить его
import os
os.chdir('/mnt')
f = os.getcwd()
print(f)
'''

#import os
# создаем каталог os.mkdir('python_folder')
# удаляем каталог os.rmdir('python_folder')
# позволяет выводить содержимое файла в.ч и скрытые папки f = os.listdir('/mnt')
#позволяет получить дерево каталогов
# for (p,d,f) in os.walk('/mnt/data/video'): print(p)
