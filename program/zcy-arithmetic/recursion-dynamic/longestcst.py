#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   longestcst.py
    @Time    :   2019/08/30 21:45:14
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    最长公共子串问题
'''


# here put the import lib

def getdp1(s1, s2):
    dp = [[0]*len(s2) for _ in range(len(s1))]

    for i in range(len(s1)):
        if s1[i] == s2[0]:
            dp[i][0] = 1
    for j in range(1, len(s2)):
        if s2[j] == s1[0]:
            dp[0][j] = 1

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1]+1

    return dp


def lcst1(s1, s2):
    dp = getdp1(s1, s2)
    end = 0
    star = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            if dp[i][j] > star:
                end = i
                star = dp[i][j]

    return s1[end-star+1:end+1]


def lcst2(s1, s2):
    if not s1 or not s2:
        return ''

    row = 0
    col = len(s2)-1
    star = 0
    end = 0

    while row < len(s1):
        i = row
        j = col
        l = 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                l = 0
            else:
                l += 1
            if l > star:
                end = i
                star = l
            i += 1
            j += 1
        if col > 0:
            col -= 1
        else:
            row += 1
    return s1[end-star+1:end+1]


s1 = '1AB2345CD'
s2 = '12345EF'
print(lcst1(s1, s2),'l1')
print(lcst2('1AB2345CD', '12345EF'),'l2')
