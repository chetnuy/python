'''
# простой пузырьковый алгоритм поиска
f = [1,3,5,3,6,7,2,9,0,2,6,3,22]
print(f)
f[2] = 9
print(f)
print(f.__len__())
for z in range(f.__len__()-1):
    for i in range(f.__len__()-1):
        if f[i]< f[i+1]:
            x = f[i]
            f[i] = f[i+1]
            f[i+1] = x
print(f)
'''

'''
# рандомный массив с поиском большего значения
import random, math
y = int(input('Input size array: '))
c=[]
for i in range(y):
     c.append(random.randrange(0,10))
print(c)
for z in range(y-1):
    if c[z]>c[z+1]:
        v =c[z]


print(v)
print (max(c))
'''

# c = [4,5,2,8,1]
# t = c.index(max(c)) # ищем индекс большего элемента
# c[-1],c[t] = c[t],c[-1] # меняем местами последний элемент и больший
#
# print(c)

'''
# перемешиваем массив
import random
f = [3,4,5,1,2,]
print(f)
for x in range(f.__len__()):
    z = random.randrange(0,f.__len__())
    f[x],f[z] = f[z],f[x]
print(f)
'''
# f =[2,3,4,5,6,3,1,2,3,3,0]
# print(f)
# count = [0]* (max(f)+1)
# new = []
# #count = [0]* f.__len__()
# print(count)
# for i in f:
#     count[i] +=1
# print(count)
# for i in range(len(count)):
#     new += [i] * count[i]
#
# print(new)

#Сортировка вставками

# array = [1,3,7,2,3,7,34,9]
#
# for i in range(len(array)):
#     while array[i] < array[i - 1]:
#          array[i], array[i - 1] = array[i - 1], array[i]
#          print(i)
#
# print(array)

