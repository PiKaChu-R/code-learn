#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   rectCover.py
    @Time    :   2019/09/09 10:12:21
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
    请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''


# here put the import lib

def rectCover(n):
    if n <= 2:
        return n

    a, b = 0, 1
    for _ in range(n+1):
        a, b = b, a+b
    return a
