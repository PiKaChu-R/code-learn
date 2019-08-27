#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   minPath.py
    @Time    :   2019/08/27 22:22:42
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    题目：给定一个矩阵M，从左上角开始每次只能向右或向下走，最后到达右下角的位置，
        路径上所有的数字累加起来就是路径和，返回所有的路径和中最小的路径和。
'''


# here put the import lib

# O(m*n) 空间O(m*n)

def solution(m):
    if len(m) == 0 or len(m[0]) == 0:
        return 0

    row = len(m)
    col = len(m[0])
    dp = [[0]*col for _ in range(row)]
    dp[0][0] = m[0][0]

    for i in range(1, row):
        dp[i][0] = dp[i-1][0] + m[i][0]

    for j in range(1, col):
        dp[0][j] = dp[0][j-1] + m[0][j]

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + m[i][j]

    return dp[-1][-1]


def solution2(m):
    if len(m) == 0 or len(m[0]) == 0:
        return 0

    more = max(len(m), len(m[0]))
    less = min(len(m), len(m[0]))
    if more == len(m):
        flag = True
    else:
        flag = False
    arr = [0] * less
    arr[0] = m[0][0]

    for i in range(1, less):

        # if flag:
        #     arr[i] = arr[i-1] + m[0][i]
        # else:
        #     arr[i] = arr[i-1] +  m[i][0]
        arr[i] = arr[i-1] + (m[0][i] if flag else m[i][0])

    for i in range(1,more):
        arr[0] = arr[0] + (m[i][0] if flag else m[0][i])
        for j in range(1,less):
            arr[j] = min(arr[j-1],arr[j]) + (m[i][j] if flag else m[j][i])
    
    return arr[-1]

m = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
print(solution(m))
print(solution2(m))