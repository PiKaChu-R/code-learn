#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   movingCount.py
    @Time    :   2019/09/16 19:10:39
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
    例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
    但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''


# here put the import lib
class Solution:
    def movingCount(self, threshold, rows, cols):
        if rows <= 0 or cols <= 0:
            return None

        def sumall(a, b):
            return sum([int(i) for i in str(a)]) + sum([int(j) for j in str(b)])

        def moving(i, j, visited):
            if i >= rows or j >= cols or i < 0 or j < 0:
                return 0
            if (i, j) in visited:
                return 0
            if sumall(i, j) > threshold:
                return 0
            visited.add((i, j))

            return 1 + moving(i-1, j, visited)+moving(i+1, j, visited)+moving(i, j+1, visited)+moving(i, j-1, visited)

        k = set()
        count = moving(0, 0, k)
        return count
