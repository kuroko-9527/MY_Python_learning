# timeit 模块 需要接收三个参数
#
# class timeit.Timer(stmt="pass",setup="pass",timer=<timer funcation>)
# Timer是用来测量小段代码执行速度的类。
# stmt参数是要测试的代码语句（statment）
# setup参数是运行代码时需要的设置
# timer参数是一个定时器函数，与平台有关
#
# timeit.Timer.timeit(number=100000)
# Timer类中测试语句执行速度的对象方法，测算number次取回平均值

import timeit
from timeit import Timer

def test1(): # 列表后边追加 一个元素
    li = []
    for i in range(10000):
        li.append(i)

def test2(): # 生成一个新列表
    li = []
    for i in range(10000):
        li = li + [i]

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))
    # 第一个参数是代码并不是函数本身

def test5(): # list列表对象在后面进行扩充  扩充的是可迭代对象或者列表
    li = []
    for i in range(10000):
        li.extend([i])

timer1 =Timer("test1()","from __main__ import test1")
print("append:",timer1.timeit(2000))
timer2 =Timer("test2()","from __main__ import test2")
print("+:",timer2.timeit(2000))
timer3 =Timer("test3()","from __main__ import test3")
print("[i for i in range]:",timer3.timeit(2000))
timer4 =Timer("test4()","from __main__ import test4")
print("list(range()):",timer4.timeit(2000))
timer5 =Timer("test5()","from __main__ import test5")
print("Extend:",timer5.timeit(2000))

# append: 1.6236466410000001
# +: 500.754945566+
# [i for i in range]: 0.7409286720000003
# list(range()): 0.3553110539999995
# Extend: 2.47068201

def t6():
    li = []
    for i in range(10000):
        li.append(i)

def t7():
    li = []
    for i in range(10000):
        li.insert(0,i)

timer6 =Timer("t6()","from __main__ import t6")
print("append:",timer6.timeit(2000))
timer7 =Timer("t7()","from __main__ import t7")
print("insert(0):",timer7.timeit(2000))

# append: 1.606771156
# insert(0): 44.188735906999995 头部添加
# 数据的存储方式决定的
