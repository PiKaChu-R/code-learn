#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   longestcse.py
    @Time    :   2019/08/30 21:18:33
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    最长公共子序列:建立一个n*m的矩阵。
'''


# here put the import lib

def getdp(s1,s2):
    dp = [[0]* len(s2) for _ in range(len(s1))]
    if s1[0] == s2[0]:
        dp[0][0] = 1
    
    for i in range(1,len(s1)):
        if s1[i] == s2[0]:
            tmp = 1
        else:
            tmp =0
        dp[i][0] = max(dp[i-1][0],tmp)
    
    for j in range(1,len(s2)):
        if s2[j] == s1[0]:
            tmp = 1
        else:
            tmp = 0
        dp[0][j] = max(dp[0][j-1],tmp)
    
    for i in range(1,len(s1)):
        for j in range(1,len(s2)):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if s1[i] == s2[j]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1)
    
    return dp

def lcse(s1,s2):
    if not s1 or not s2:
        return ''
    
    dp = getdp(s1,s2)
    m = len(s1) - 1
    n = len(s2) - 1 
    res = ''
    index = dp[-1][-1]
    print(index,dp)
    while index > 0:
        if n > 0 and dp[m][n] == dp[m][n-1]:
            n -= 1
        elif m>0 and dp[m][n] == dp[m-1][n]:
            m -= 1
        else:
            res += s1[m]
            m -= 1
            n -= 1
            index -= 1
    return res[::-1]

s1 = '1A2C3D4B56'
s2 = 'B1D23CA45B6A'

print(lcse(s1,s2))

