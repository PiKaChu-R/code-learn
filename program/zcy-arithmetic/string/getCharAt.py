#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   getCharAt.py
    @Time    :   2019/09/05 21:32:59
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    给定统计字符串，给定一个整数index，返回第index个字符。
'''


# here put the import lib

def getCharAt(s, index):
    if not s:
        return 0

    stage = True
    cur = 0
    num = 0
    count = 0
    i = 0
    while i != len(s):
        if s[i] == '_':
            stage = not stage
        else:
            if stage:
                count += num
                if count > index:
                    return cur
                num = 0
                cur = s[i]
            else:
                num = num * 10 + int(s[i])
        i += 1
    if count + num > index:
        return cur
    else:
        return 0

print(getCharAt('a_1_b_100',50))
