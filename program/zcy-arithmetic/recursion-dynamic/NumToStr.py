#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   NumToStr.py
    @Time    :   2019/09/02 22:29:27
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
'''


# here put the import lib

# 暴利递归，时间O(2^n)，空间O(n)
def num1(s):
    if s == None or s == '':
        return 0
    return process(s, 0)


def process(s, i):
    if i == len(s):
        return 1
    if s[i] == '0':
        return 0

    res = process(s, i+1)
    if i+1 < len(s) and s[i:i+2] < '27':
        res += process(s, i+2)

    return res

# 时间O(n)，空间O(1)
def num2(s):
    if s == None or s == '':
        return 0
    n = len(s)
    if s[-1] == '0':
        cur = 0
    else:
        cur = 1
    last = 1
    tmp = 0
    for i in range(n-2,-1,-1):
        if s[i] == '0':
            last = cur
            cur = 0
        else:
            tmp = cur
            if s[i:i+2] < '27':
                cur += last
            last = tmp
    return cur

s = '1111'
print(num1(s))
print(num2(s))
