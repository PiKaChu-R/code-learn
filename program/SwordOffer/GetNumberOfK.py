#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   GetNumberOfK.py
    @Time    :   2019/09/09 16:18:33
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    统计一个数字在排序数组中出现的次数。
'''


# here put the import lib
class Solution:
    def GetNumberOfK(self,data,k):
        n = len(data)
        left = 0
        right = n-1
        count = 1
        index = -1
        while left <= right:
            mid = left + (right-left)//2
            if data[mid] > k:
                right = mid - 1
                continue
            if data[mid] < k:
                left = mid + 1
                continue
            if data[mid] == k:
                index = mid
                break
        if index == -1:
            return 0
        low = index - 1
        high = index + 1
        while low >= 0 and data[low] == k:
            count += 1
            low -= 1
        while high < n and data[high] == k:
            count += 1
            high += 1
        return count