#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Power.py
    @Time    :   2019/09/09 10:18:04
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
    保证base和exponent不同时为0
'''


# here put the import lib
def Power(base, exponent):
    if base == 0:
        return 0
    if exponent == 0 or base == 1:
        return 1
    result = 1
    for i in range(abs(exponent)):
        result *= base
    if exponent < 0:
        result = 1/result

    return result
