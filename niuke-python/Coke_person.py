#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Coke_person.py
    @Time    :   2019/04/18 17:18:22
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    小 S，小L，小P，小R，小H队列的第一个人 （小S）买了一听可乐，喝下去后变成了两个小S！
    然后两个小S心满意足的站到了队伍的最后。此时队形变成了这样：
    小 L，小P，小R，小H，小S，小S 然后队列中下一个人 （小L）也买了听可乐，喝下去后变成
    两个人，站到了队伍最后。以此类推。例如小P第三个喝了克隆可乐，之后队伍变成这个样子：
    小 R，小H，小S，小S，小L，小L，小P，小P
    请问第 n个喝这个饮料的人是谁？
'''


# here put the import lib

list_person = ['S','L','P','R','H']

n = int(input())

for i in range(1,n+1):
    m = list_person[0]
    list_person.pop(0)
    list_person.append(m)
    list_person.append(m)
print(list_person[-1],list_person)

