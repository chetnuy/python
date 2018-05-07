#Вывод содержимого каталога
import os

dir = '/mnt/trash'
files = os.listdir(dir)

#построчный вывод содержимого
for i in files:
    print(i)

#вывод только определенных файлов
images = filter(lambda x: x.endswith('.gz'), files)
print(images)
