'''
class Myclass:
    def __init__(self):
        self.x = 777
    def get_x(self):
        return self.x

c = Myclass()
print(getattr(c,'x'))
print(getattr(c,'get_x')())
print(getattr(c,'y',0))
setattr(c,'y',20)
print(getattr(c,'y',0))
delattr(c,'x')
print(getattr(c,'x',0))
print(hasattr(c,'x'))
print(hasattr(c,'y'))

'''

'''
#работа с конструктором и деструктором
class Myclass:
    def __init__(self):
        print('create object')
    def __del__(self):
        print('del object')
    x = 10
c = Myclass()
print(Myclass.x)
del c
'''

'''
class MyClass1:
    def fun1(self):
        print('this fun1')
class MyClass2:
    def fun2(self):
        print('this fun2')

class MyClass3(MyClass1,MyClass2):
    def __init__(self):
        print('this constructor')
    def fun3(self):
        print('this fun3')
    def __del__(self):
        print("this destructor")
'''
'''
#Множественное наследование
c = MyClass3()
c.fun1()
c.fun2()
c.fun3()
print(MyClass1.__bases__)
print(MyClass2.__bases__)
print(MyClass3.__bases__)
print(MyClass3.__mro__)
'''
'''
# Перегрузка операторов
x = 10
y = 20

x.__add__(y)
print(x.__add__(y))
'''

'''
try:
    x = 1/0
    print(x)
except Exception as err: # Exception - позволяет обрабатывать все виды ошибок
    print('no division zero')
finally:
    print('i coal ever')

'''

