#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   NumberOf1.py
    @Time    :   2019/09/09 10:14:35
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''


# here put the import lib
def NumberOf1(n):
    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n :
        count += 1
        n = n&(n-1)
    return count 