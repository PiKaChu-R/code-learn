#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   longestConsecutive.py
    @Time    :   2019/09/04 17:00:40
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    数组中的最长连续序列
    给定无序数组arr，返回其中最长的连续序列长度。
    利用哈希表可以实现时间O(n)，空间O(n)。
'''


# here put the import lib

def longestConsecutive(arr):
    if arr == None or len(arr) == 0:
        return 0
    
    _max = 1
    d = dict()

    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 1
            if arr[i] -1 in d:
                _max = max(_max,merge(d,arr[i]-1,arr[i]))
            if arr[i]+1 in d:
                _max = max(_max,merge(d,arr[i],arr[i]+1))
    print(d)
    return _max

def merge(d,less,more):
    
    left = less-d.get(less) +1
    right = more+d.get(more) -1
    l = right-left+1
    d[left] = l
    d[right] = l
    return l

arr = [100,101,104,103,200,102]
print(longestConsecutive(arr))