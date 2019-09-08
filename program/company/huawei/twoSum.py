#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   twoSum.py
    @Time    :   2019/09/08 20:52:56
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    数组中两数之和=给定目标值
'''


# here put the import lib
def twoSum(nums,target):
    n = len(nums)
    lookup = {}
    for i in range(n):
        tmp = target - nums[i]
        if tmp in lookup:
            return [lookup[tmp],i]
        lookup[nums[i]] = i
    return -1