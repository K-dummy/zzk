#1、编写一个Animal类，属性有name，方法有call()；
#现有Dog类和Cat类继承Animal类，请根据实际情况重写call() （比如，狗叫可以打印汪汪，猫叫可以打印喵喵）

class Animal():
    name = ''
    def call():
        print('super Animal')

class Dog(Animal):
    def call():
        print("wang wang")

class Cat(Animal):
    def call():
        print("maio miao")


#2、使用递归实现10以内的斐波那契数列

def fib(x):
    if x <= 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

#3、使用列表推导获取100以内的奇数

lst = [print(i) for i in range(0,101)if i % 2 == 1]

#4、使用异常处理结构实现 add(x,y) / sub(x,y) / mul(x,y) / div(x,y)

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

import pdb
def test():
    try:
        print("try")
        print(add(10,0))
        print(sub(10,0))
        print(mul(10,0))
        print(div(10,0))
    except:
        print(sys.exc_info())

#5、将Python之禅（import this）写入文件，并统计有多少单词及其出现的次数，将统计结果序列化至文件中保存

import json

