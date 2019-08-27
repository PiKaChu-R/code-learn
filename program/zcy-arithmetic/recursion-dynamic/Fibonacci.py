#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Fibonacci.py
    @Time    :   2019/08/27 21:32:47
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    题目：给定整数N，返回斐波那契数列的第N项。
    类似题目：跳台阶。
    跳台阶中计算最后的值的结果时用的是（2,1）。
'''


# here put the import lib

# O(n)的解法

def solution(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1

    res = 1
    pre = 1
    tmp = 0

    for i in range(3, n+1):
        tmp = res
        res += pre
        pre = tmp

    return res

# O(logn)的解法


def solution2(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1

    base = [[1, 1], [1, 0]]
    res = matrixPower(base, n-2)
    return res[0][0] + res[1][0]


def matrixPower(m, p):
    res = [[0]*len(m[0]) for _ in range(len(m))]

    for i in range(len(res)):
        res[i][i] = 1

    tmp = m
    while p != 0:

        if (p & 1) != 0:
            res = muliMatrix(res, tmp)
        tmp = muliMatrix(tmp, tmp)
        p = p >> 1
    return res


def muliMatrix(m1, m2):
    res = [[0]*len(m2[0]) for _ in range(len(m1))]

    for i in range(len(m2[0])):
        for j in range(len(m1)):
            for k in range(len(m2)):
                res[i][j] += m1[i][k] * m2[k][j]
    return res


print(solution(10))
print(solution2(10))
