#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   minCostEdit.py
    @Time    :   2019/08/31 20:33:13
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
'''


# here put the import lib

# 时间复杂度为O(MxN)，s1长度为M，s2长度为N，额外空间复杂度为O(MxN)


def minCostEdit1(s1, s2, ic, dc, rc):
    if not s1 or not s2:
        return 0

    row = len(s1)+1
    col = len(s2)+1

    dp = [[0]*col for _ in range(row)]

    for i in range(1,row):
        dp[i][0] = dc * i
    for j in range(1,col):
        dp[0][j] = ic * i
    
    for i in range(1,row):
        for j in range(1,col):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + rc
            dp[i][j] = min(dp[i][j],dp[i][j-1]+ic)
            dp[i][j] = min(dp[i][j], dp[i-1][j]+dc)
    return dp[row-1][col-1]
    
# 结合压缩空间的技巧，空间复杂度可以压缩到O(min{M,N})
def minCostEdit2(s1,s2,ic,dc,rc):
    if not s1 or not s2:
        return 0

    if len(s1) >= len(s2):
        longs = s1
        shorts = s2
    else:
        longs = s2
        shorts = s1
    
    if len(s1) < len(s2):
        ic,dc = dc,ic
    
    dp = [0] * (len(shorts)+1)
    for i in range(1,len(shorts)+1):
        dp[i] = ic*i
    
    for i in range(1,len(longs)+1):
        pre = dp[0]
        dp[0] = dc * i
        for j in range(1,len(shorts)+1):
            tmp = dp[j]
            if longs[i-1] == shorts[j-1]:
                dp[j] = pre
            else:
                dp[j] = pre + rc
            dp[j] = min(dp[j],dp[j-1]+ic)
            dp[j] = min(dp[j],tmp+dc)
            pre = tmp
    return dp[len(shorts)]

s1 = 'ab12cd3'
s2 = 'abcdf'
ic = 5
dc = 3
rc = 2
print(minCostEdit1(s1,s2,ic,dc,rc))
print(minCostEdit2(s1,s2,ic,dc,rc))

# 最少编辑次数：LeetCode -72
class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [ [0] * (n + 1) for _ in range(m + 1)]
        # print(dp)
        for i in range(n+1):
            dp[0][i] = i
        # print(dp)
        for i in range(m+1):
            dp[i][0] = i
        
        # print(dp)
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
        return dp[-1][-1]