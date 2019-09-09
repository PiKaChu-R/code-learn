#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   FindNumbersWithSum.py
    @Time    :   2019/09/09 16:55:37
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
    如果有多对数字的和等于S，输出两个数的乘积最小的。
    对应每个测试案例，输出两个数，小的先输出。
'''


# here put the import lib
def FindNumbersWithSum(array, tsum):
    if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
        return []

    left = 0
    right = len(array) - 1
    while left < right:
        tmp = array[left] + array[right]
        if tmp == tsum:
            return [array[left], array[right]]
        elif tmp > tsum:
            right -= 1
        else:
            left += 1
    return []