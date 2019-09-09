#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   IsContinuous.py
    @Time    :   2019/09/09 17:12:10
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
'''


# here put the import lib
def IsContinuous(nums):
    if not nums:
        return False
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        if i > 0 and nums[i] == nums[i-1]:
            return False
        if nums[-1]- nums[i] >4:
            return False
    return True

def IsContinuous2(nums):
    if not nums:
        return False
    nums.sort()
    zero = nums.count(0)
    for i,v in enumerate(nums[:-1]):
        if v != 0:
            if nums[i+1] == v:
                return False
            zero = zero - (nums[i+1] - v - 1)
            if zero < 0:
                return False
    return True