#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   generateLIS.py
    @Time    :   2019/08/28 11:28:10
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    最长递增子序列
'''


# here put the import lib

def solution(arr):
    if len(arr) == 0:
        return None

    # dp = getdp1(arr)
    dp = getdp2(arr)
    return generateLIS(arr, dp)

# 常规，时间O(n^2)


def getdp1(arr):
    dp = [0] * len(arr)
    for i in range(len(arr)):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return dp


# 采用二分查找，时间O(NlogN)

def getdp2(arr):
    dp = [0] * len(arr)
    ends = [0] * len(arr)
    ends[0] = arr[0]
    dp[0] = 1
    right = 0

    for i in range(1, len(arr)):
        l = 0
        r = right
        while l <= r:
            m = (l+r)//2
            if arr[i] > ends[m]:
                l = m + 1
            else:
                r = m - 1
        right = max(right, l)
        ends[l] = arr[i]
        dp[i] = l+1
    return dp


def generateLIS(arr, dp):
    length = 0
    index = 0
    for i in range(len(dp)):
        if dp[i] > length:
            length = dp[i]
            index = i

    lis = [0] * length
    length -= 1
    lis[length] = arr[index]
    length -= 1
    for i in range(index, -1, -1):
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:
            lis[length] = arr[i]
            index = i
            length -= 1
    return lis


arr = [2, 1, 5, 3, 6, 4, 8, 9, 7]
print(solution(arr))
