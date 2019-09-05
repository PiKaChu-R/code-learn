#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   removeKZeros.py
    @Time    :   2019/09/05 19:42:55
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    去除字符串中连续出现的k个零，返回处理后的字符串。
    时间O(n)，空间O(1)
'''


# here put the import lib
def removeKZeros(s, k):
    if not s or k < 1:
        return s

    count = 0
    start = -1
    i = 0
    while i < len(s):
        if s[i] == '0':
            if start == -1:
                start = i
            count += 1
        else:
            if count == k:
                s = s[:start]+s[start+count:]
                i -= count 
            count = 0
            start = -1
        i += 1
    if count == k:
        s = s[:start]+s[start+count:]

    return s


print(removeKZeros('0', 1))