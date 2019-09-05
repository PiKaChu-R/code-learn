#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   replace.py
    @Time    :   2019/09/05 20:36:46
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    替换字符串中连续出现的指定字符串
'''


# here put the import lib
def replace(s, f, t):
    if not s or not f:
        return s
    s = list(s)
    match = 0
    for i in range(len(s)):
        if s[i] == f[match]:
            match += 1
            if match == len(f):
                clear(s, i, len(f))
                match = 0
        else:
            match = 0

    res = ''
    cur = ''
    for i in range(len(s)):
        if s[i] != 0:
            cur += s[i]
        if s[i] == 0 and (i == 0 or s[i-1] != 0):
            res = res+cur+t
            cur = ''
    if cur:
        res = res + cur
    return res

def clear(s,end,l):
    while l != 0:
        s[end] = 0
        end -= 1
        l -= 1

s = '123abc123abc'
f = 'abc'
t = 'X'
print(replace(s,f,t))