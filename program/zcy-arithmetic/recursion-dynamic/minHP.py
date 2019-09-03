#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   minHP.py
    @Time    :   2019/09/02 19:31:25
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    龙与地下城——计算时从右下角开始计算，选择从右至左，从下到上的计算方式即可。
    类似题：矩阵行走，每个坐标存在价值大小或阻碍，行走方式只能向下或向右
'''


# here put the import lib

# 经典动态规划方法的时间复杂度为O(MxN)，额外的空间复杂度为O(MxN)

def minHP1(m):
    if not m or not m[0]:
        return 1
    
    row = len(m)
    col = len(m[0])
    dp = [[0]*col for _ in range(row)]
    dp[row-1][col-1] = max(-m[row-1][col-1]+1, 1)
    row -= 1
    col -= 1

    for j in range(col-1,-1,-1):
        dp[row][j] = max(dp[row][j+1]-m[row][j],1)
    
    for i in range(row-1,-1,-1):
        dp[i][col] = max(dp[i+1][col]-m[i][col],1)
        for j in range(col-1,-1,-1):
            right = max(dp[i][j+1]-m[i][j],1)
            left = max(dp[i+1][j]-m[i][j],1)
            dp[i][j] = min(right,left)
    # print(dp)
    return dp[0][0]

# 时间复杂度没变，空间复杂度减小O(min{M,N})
def minHP2(m):

    if m == None or m[0] == None or len(m[0]) == 0 or len(m) == 0:
        return 1
    
    more = len(m) if len(m) >= len(m[0]) else len(m[0])
    less = len(m) if len(m) < len(m[0]) else len(m[0])
    rowmore = True if more == len(m) else False
    dp = [0] * less
    dp[-1] = max(-m[more-1][less-1]+1,1)

    for i in range(less-2,-1,-1):
        row = more-1 if rowmore else i
        col = i if rowmore else more-1
        dp[i] = max(dp[i+1]-m[row][col],1)
    
    for i in range(more-2,-1,-1):
        row = i if rowmore else less-1
        col = less-1 if rowmore else i
        dp[-1] = max(1,dp[-1]-m[row][col])
        for j in range(less-2,-1,-1):
            row = i if rowmore else j
            col = j if rowmore else i
            right = max(1,dp[j+1]-m[row][col])
            down = max(1,dp[j]-m[row][col])
            dp[j] = min(right,down)
    return dp[0]



m = [[-2,-3,3],[-5,-10,1],[0,30,-5]]
print(minHP1(m))
print(minHP2(m))