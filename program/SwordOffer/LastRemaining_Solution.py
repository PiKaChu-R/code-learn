#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   LastRemaining_Solution.py
    @Time    :   2019/09/09 17:20:02
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字
    求这个圆圈中最后剩下的一个数字
'''


# here put the import lib
def LastRemaining_Solution(n,m):
    if n < 1 or m < 1:
        return -1
    last = 0
    for i in range(1,n+1):
        last = (last + m)%i
    return last+1

print(LastRemaining_Solution(8,4))