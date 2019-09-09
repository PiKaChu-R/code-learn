#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   ReverseSentence.py
    @Time    :   2019/09/09 17:08:31
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个英文句子, 翻转句子中单词的顺序,但单词内字符的顺序不变
    为简单起见, 标点符号和普通字母一样处理
'''


# here put the import lib
def ReverseSentence(s):
    new = s.split(' ')
    return ' '.join(new[::-1])
