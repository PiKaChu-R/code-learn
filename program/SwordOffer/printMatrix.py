#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   printMatrix.py
    @Time    :   2019/09/09 11:09:18
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
    如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''


# here put the import lib
def printMatrix(matrix):
    if not matrix:
        return []

    ans = []
    while matrix:
        ans.extend(matrix.pop(0))
        if not matrix:
            break
        next_matrix = []
        for x in zip(*matrix):
            next_matrix.append(x)
        matrix = next_matrix[::-1]
    return ans
