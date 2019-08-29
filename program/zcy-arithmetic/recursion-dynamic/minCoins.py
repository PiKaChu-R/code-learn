#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   minCoins.py
    @Time    :   2019/08/27 22:49:48
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    换钱的最少货币数
'''


# here put the import lib

# O(N*aim) 时间空间均是

def solution(arr, aim):
    if len(arr) == 0 or aim < 0:
        return -1

    n = len(arr)
    max_n = float('inf')
    dp = [[0]*(aim+1) for _ in range(n)]

    for i in range(1, aim+1):
        dp[0][i] = max_n
        if i-arr[0] >= 0 and dp[0][i-arr[0]] != max_n:
            dp[0][i] = dp[0][i-arr[0]]+1

    left = 0
    for i in range(1, n):
        for j in range(1, aim+1):
            left = max_n
            if j-arr[i] >= 0 and dp[i][j-arr[i]] != max_n:
                left = dp[i][j-arr[i]]+1
            dp[i][j] = min(left, dp[i-1][j])

    return dp[n-1][aim] if dp[n-1][aim] != max_n else -1


# 压缩空间，时间：O(N*aim)，空间O(aim)
def solution2(arr, aim):
    if len(arr) == 0 or aim < 0:
        return -1

    n = len(arr)
    max_n = float('inf')
    dp = [0]*(aim+1)

    for i in range(1, aim+1):
        dp[i] = max_n
        if i-arr[0] >= 0 and dp[i-arr[0]] != max_n:
            dp[i] = dp[i-arr[0]]+1

    left = 0
    for i in range(1, n):
        for j in range(1, aim+1):
            left = max_n
            if j-arr[i] >= 0 and dp[j-arr[i]] != max_n:
                left = dp[j-arr[i]]+1
            dp[j] = min(left, dp[j])

    return dp[aim] if dp[aim] != max_n else -1


arr = [5, 2, 3]
aim = 20

print(solution(arr, aim))
print(solution2(arr, aim))

# arr中每个位置上的钱数，只能使用一次。

# 空间复杂度最低版本


def solution3(arr, aim):
    if len(arr) == 0 or aim < 0:
        return -1

    n = len(arr)
    max_n = float('inf')
    dp = [0] * (aim+1)

    for j in range(1, aim+1):
        dp[j] = max_n
    if arr[0] <= aim:
        dp[arr[0]] = 1

    left = 0

    for i in range(1, n):
        for j in range(aim, 0, -1):
            left = max_n
            if j - arr[i] >= 0 and dp[j-arr[i]] != max_n:
                left = dp[j-arr[i]]+1
            dp[j] = min(left, dp[j-1])

    return dp[aim] if dp[aim] != max_n else -1

arr = [5, 2, 3]
aim = 20

print(solution3(arr, aim))