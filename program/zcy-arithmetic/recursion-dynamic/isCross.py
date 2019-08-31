#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   isCross1.py
    @Time    :   2019/08/31 22:04:29
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    字符串的交错组成。s1 = 'ab',s2 = '12',那么'ab12','a1b2'等都是s1和s2的交错组成。
'''


# here put the import lib

# 经典动态规划时间复杂度O(MxN)，空间复杂度O(MxN)。s1长度为M,s2长度为N

def isCross1(s1, s2, aim):
    if not s1 or not s2 or not aim:
        return False

    if len(aim) != (len(s1)+len(s2)):
        return False

    dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
    dp[0][0] = True
    for i in range(1, len(s1)+1):
        if s1[i-1] != aim[i-1]:
            break
        dp[i][0] = True
    for j in range(1, len(s2)+1):
        if s2[j-1] != aim[j-1]:
            break
        dp[0][j] = True

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if (s1[i-1] == aim[i+j-1] and dp[i-1][j]) or(s2[j-1] == aim[i+j-1] and dp[i][j-1]):
                dp[i][j] = True

    return dp[-1][-1]

# 采用空间压缩的方法，时间复杂度为O(min{M,N})


def isCross2(s1, s2, aim):
    if not s1 or not s2 or not aim:
        return False

    if len(aim) != (len(s1)+len(s2)):
        return False
    
    if len(s1)>= len(s2):
        longs = s1
        shorts = s2
    else:
        longs = s2
        shorts = s1
    dp = [False] * (len(shorts)+1)
    dp[0] =True

    for i in range(1,len(shorts)+1):
        if shorts[i-1] != aim[i-1]:
            break
        dp[i] = True
    
    for i in range(1,len(longs)+1):
        dp[0] = dp[0] and longs[i-1] == aim[i-1]
        for j in range(1,len(shorts)+1):
            if longs[i-1] == aim[i-1+j] and dp[j] or (shorts[j-1] == aim[i+j-1] and dp[j-1]):
                dp[j] = True
    return dp[-1]


s1 = 'AB'
s2 = '12'
aim = 'A12B'
print(isCross1(s1, s2, aim))
print(isCross2(s1, s2, aim))
