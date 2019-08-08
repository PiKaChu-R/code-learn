#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   01bag-dynamic.py
    @Time    :   2019/06/21 10:02:38
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   01背包问题-动态规划
'''

'''
解题思路：动态规划，对每一件物品遍历背包容量，当背包可容纳值大于等于当前物品，与之前
        已放入的物品价值进行对比，考虑是否需要置换。

'''


# here put the import lib
"""
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
"""

def bag(n,c,w,v):
    value = [[0 for j in range(c+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            value[i][j] = value[i-1][j]
            if j >= w[i-1] and value[i][j]<value[i-1][j-w[i-1]]+v[i-1]:
                value[i][j] = value[i-1][j-w[i-1]]+v[i-1]
    for x in value:
        print(x)
    return value

def show(n,c,w,value):
    print('最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个,', end='')

def bag2(n,c,w,v):

    #无法确定具体物品是哪几个
    values = [0 for i in range(c+1)]

    for i in range(1,n+1):
        for j in range(c,0,-1):
            if j >=w[i-1]:
                values[j] = max(values[j-w[i-1]]+v[i-1],values[j])
    return value


if __name__ == '__main__':
    n = 6
    c = 10
    w = [2, 2, 3, 1, 5, 2]
    v = [2, 3, 1, 5, 4, 3]
    value = bag(n, c, w, v)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # [0, 0, 3, 3, 5, 5, 5, 5, 5, 5, 5]
    # [0, 0, 3, 3, 5, 5, 5, 6, 6, 6, 6]
    # [0, 5, 5, 8, 8, 10, 10, 10, 11, 11, 11]
    # [0, 5, 5, 8, 8, 10, 10, 10, 12, 12, 14]
    # [0, 5, 5, 8, 8, 11, 11, 13, 13, 13, 15]
    show(n, c, w, value)
    # 最大价值为: 15
    # 背包中所装物品为:
    # 第 2 个,第 4 个,第 5 个,第 6 个,
    print('\n空间复杂度优化为N(c)结果:', bag2(n, c, w, v))
