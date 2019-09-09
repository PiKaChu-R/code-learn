#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Add.py
    @Time    :   2019/09/09 17:35:27
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''


# here put the import lib
def Add(num1,num2):
    while num2 != 0:
        tmp = num1 ^ num2
        num2 = (num1 & num2) << 1
        num1 = tmp & 0xffffffff
    return num1 if num1 >>31 == 0 else num1 - 4294967296