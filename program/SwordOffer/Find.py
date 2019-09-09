#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Find.py
    @Time    :   2019/09/09 08:56:38
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
    每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
    整数，判断数组中是否含有该整数。
'''


# here put the import lib
def Find(array,target):
    if not array or not target :
        return False

    row = len(array)
    col = len(array[0])

    if col == 0:
        return False
    if target > array[-1][-1] or target < array[0][0]:
        return False
    
    for i in range(row):
        if target > array[i][-1] or target < array[i][0]:
            continue
        for j in range(col):
            if target == array[i][j]:
                return True
    return False

def Find2(array,target):
    row = len(array)
    col = len(array[0])

    i = 0
    j = col-1
    while i < row and j >= 0:
        if array[i][j] > target:
            j -= 1
        elif array[i][j] < target:
            i += 1
        else:
            return True
    return False