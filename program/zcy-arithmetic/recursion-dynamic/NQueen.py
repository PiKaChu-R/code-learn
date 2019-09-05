#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   NQueen.py
    @Time    :   2019/09/05 17:02:39
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    N皇后问题，返回的是n皇后的摆法有多少。
'''


# here put the import lib
# 递归过程设计成逐行放置皇后的方式。
# record代表的是第几行以及每行第几列放置物品。

def num1(n):
    if n<1:
        return 0
    record = [0]*n
    return process1(0,record,n)

def process1(i,record,n):
    if i == n:
        return 1
    res = 0
    for j in range(n):
        if isVaild(record,i,j):
            record[i] = j
            res += process1(i+1,record,n)
    return res

def isVaild(record,i,j):
    for k in range(i):
        if j == record[k] or abs(record[k]-j) == abs(i-k):
            return False
    return True


def num2(n):
    # 采用位运算，只能算1-32皇后问题。
    if n<1 or n>32:
        return 0
    if n == 32:
        upperLim = -1
    else:
        upperLim = (1<<n)-1
    
    return process2(upperLim,0,0,0)

def process2(upperLim,colLim,leftLim,rightLim):
    if colLim == upperLim:
        return 1
    pos = 0
    mostRightOne = 0
    pos = upperLim & (~(colLim|leftLim|rightLim))
    res = 0
    while pos != 0:
        mostRightOne = pos & (~pos+1)
        pos = pos - mostRightOne
        res += process2(upperLim,colLim|mostRightOne,(leftLim|mostRightOne)<<1,(rightLim|mostRightOne)>>1)
    return res



print(num1(8))
print(num2(33))