#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Multiply.py
    @Time    :   2019/09/15 15:34:59
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    题目：给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素
    B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法.
    思路：
        B[0] = A[1] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[0]）
        B[1] = A[0] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[1]）
        B[2] = A[0] * A[1] * A[3] * A[4] *....*A[n-1] ;（没有A[2]）
    举例：   输入：  1   2  3  4  5
            输出：  120 60 40 30 24
    相当于一个矩形，被省去的那个数字设为1，这样的话，先把上三角的数一行一行撑起来，接着在和下三角的数相乘，节省空间
'''


# here put the import lib
class Solution:
    def Multiply(self, A):
        if not A:
            return A
        n = len(A)
        B = [1] * n
        for i in range(1, n):
            B[i] = B[i-1] * A[i-1]
        temp = 1
        for i in range(n-2, -1, -1):
            temp = temp * A[i+1]
            B[i] *= temp
        return B
