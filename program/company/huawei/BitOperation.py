#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   BitOperation.py
    @Time    :   2019/09/08 22:12:34
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    位运算-加减乘除
'''


# here put the import lib
def add1(a, b):
    # 递归
    if b == 0:
        return a
    count = a ^ b
    carry = (a & b) << 1
    return add1(count, carry)


def add2(a, b):
    # 非递归
    count = 0
    carry = 0
    while b:
        count = a ^ b
        carry = (a & b) << 1
        a = count 
        b = carry
    
    return a

print(add1(3,4))
print(add2(3,4))

# 减法
def sub1(a,b):
    return add1(a,add1(~b,1))

print(sub1(3,4))

# 乘法
def mul1(a,b):
    flag = True if (a^b)>=0 else False
    if a < 0:
        a = add1(~a,1)
    if b < 0:
        b = add1(~b,1)
    res = 0
    while b :
        if b&1:
            res = add1(res,a)
        a <<= 1
        b >>= 1
    return res if flag else add1(~res,1)

# 除法
def div(a,b):
    flag = True if (a^b)>=0 else False
    if a < 0:
        a = add1(~a,1)
    if b < 0:
        b = add1(~b,1)
    res = 0
    for i in range(31,-1,-1):
        if a >= (b << i):
            res = add1(res,1 << i)
            a = sub1(a,b << i)
    return res if flag else add1(~res,1)

print(mul1(3,4))
print(div(3,4))

