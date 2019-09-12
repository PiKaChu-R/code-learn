#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   rotateWord.py
    @Time    :   2019/09/12 21:02:25
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    翻转字符串
'''


# here put the import lib
def rotateWord(s):
    if not s :
        return 
    s = s.split()
    return ' '.join(s[::-1])

print(rotateWord('a b x'))