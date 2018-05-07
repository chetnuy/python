#читаем слова из файла и упорядочиваем их по алфовиту в другом файле

sfile='/home/nevernew/software'
dfile='/home/nevernew/soft'

for line in open(sfile):

    listWords = line.split("\t")

    print(line)
d =line.split()
d.sort()

with open(dfile, "w") as file:
    print(*d, file=file, sep=", ")