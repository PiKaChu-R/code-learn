#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   coins.py
    @Time    :   2019/08/28 09:50:18
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    换钱的方法数
'''


# here put the import lib

# 记忆化搜索的优化方式,时间O(N*aim^2)

def solution(arr, aim):
    if len(arr) == 0 or aim < 0:
        return 0

    dp = [[0]*(aim+1) for _ in range(len(arr)+1)]
    return process(arr, 0, aim, dp)


def process(arr, index, aim, dp):
    res = 0

    if index == len(arr):
        res = 1 if aim == 0 else 0
    else:
        dpVal = 0
        i = 0
        while arr[index]*i <= aim:
            dpVal = dp[index+1][aim-arr[index]*i]
            if dpVal != 0:
                if dpVal == -1:
                    res += 0
                else:
                    res += dpVal
            else:
                res += process(arr, index+1, aim-arr[index]*i, dp)
            i += 1
    dp[index][aim] = -1 if res == 0 else res
    return res

# 动态规划，时间O(N*aim^2)


def solution2(arr, aim):
    if len(arr) == 0 or aim < 0:
        return 0
    dp = [[0]*(aim+1) for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = 1
    for j in range(1, len(arr)):
        if j*arr[0] <= aim:
            dp[0][arr[0]*j] = 1

    num = 0
    for i in range(1, len(arr)):
        for j in range(1, aim+1):
            num = 0
            k = 0
            while j-arr[i]*k >= 0:
                num += dp[i-1][j-arr[i]*k]
                k += 1
            dp[i][j] = num
    return dp[len(arr)-1][aim]


# 动态规划，时间O(N*aim)，简化递推公式

def solution3(arr, aim):
    if len(arr) == 0 or aim < 0:
        return 0

    dp = [[0]*(aim+1) for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = 1
    for j in range(1, len(arr)):
        if j*arr[0] <= aim:
            dp[0][arr[0]*j] = 1

    for i in range(1, len(arr)):
        for j in range(1, aim+1):
            dp[i][j] = dp[i-1][j]
            if j-arr[i] >= 0:
                dp[i][j] += dp[i][j-arr[i]]
    return dp[-1][-1]

# 简化空间复杂度，O(aim)


def solution4(arr, aim):
    if len(arr) == 0 or aim < 0:
        return 0

    dp = [0]*(aim+1)
    for j in range(0,aim+1):
        if j*arr[0] <= aim:
            dp[arr[0]*j] = 1
    
    for i in range(1,len(arr)):
        for j in range(1,aim+1):
            if j-arr[i] >= 0:
                dp[j] += dp[j-arr[i]]
    
    return dp[aim]


arr = [5, 10, 25, 1]
aim = 15
print(solution(arr, aim))
print(solution2(arr, aim))
print(solution3(arr, aim))
print(solution4(arr, aim))
