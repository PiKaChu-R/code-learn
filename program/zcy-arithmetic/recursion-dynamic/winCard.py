#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   winCard.py
    @Time    :   2019/09/03 22:31:45
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    排成一条直线的纸牌博弈问题。
'''


# here put the import lib

# 暴利递归算法，时间O(2^n)，空间O(n)

def win1(arr):
    if arr == None or len(arr) == 0:
        return 0
    
    return max(f(arr,0,len(arr)-1),s(arr,0,len(arr)-1))

def f(arr,i,j):
    if i == j:
        return arr[i]
    return max(arr[i]+s(arr,i+1,j),arr[j]+s(arr,i,j-1))

def s(arr,i,j):
    if i==j:
        return 0
    return min(f(arr,i+1,j),f(arr,i,j-1))


# 动态规划，时间O(n^2)，空间O(n^2)
def win2(arr):
    if arr == None or len(arr) == 0:
        return 0
    f = [[0]*len(arr) for _ in range(len(arr))]
    s = [[0]*len(arr) for _ in range(len(arr))]

    for j in range(len(arr)):
        f[j][j] = arr[j]
        for i in range(j-1,-1,-1):
            f[i][j] = max(arr[i]+s[i+1][j],arr[j]+s[i][j-1])
            s[i][j] = min(f[i+1][j],f[i][j-1])
    return max(f[0][-1],s[0][-1])

arr = [1,2,100,4]
print(win1(arr))
print(win2(arr))