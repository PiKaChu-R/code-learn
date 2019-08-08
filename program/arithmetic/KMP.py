#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   KMP.py
    @Time    :   2019/07/02 20:38:04
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   KMP 
'''

'''
返回的是位置
'''


# here put the import lib
def KMP(t,p):
    if not p : return 0
    _next = [0] * len(p)

    def getNext(p, _next):
        _next[0] = -1
        i = 0
        j = -1
        while i < len(p) - 1:
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                _next[i] = j
            else:
                j = _next[j]
    getNext(p, _next)
    i = 0
    j = 0
    while i < len(t) and j < len(p):
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = _next[j]
    if j == len(p):
        return i - j
    return -1

strs = 'abbaba'
needle = "bab"

k = KMP(strs,needle)
print(k)