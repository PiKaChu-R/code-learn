#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   repalceSpace.py
    @Time    :   2019/09/09 09:04:56
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are 
    Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''


# here put the import lib

def replaceSpace(s):
    if not isinstance(s,str) or len(s) <= 0 or s == None:
        return ''
    ans = ''
    for i in s:
        if i.strip():
            ans += i
        else:
            ans += '%20'
    return ans

def replaceSpace2(s):
    return s.replace(' ','%20')

s = 'we are happy'
print(replaceSpace2(s))