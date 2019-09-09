#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   duplicate.py
    @Time    :   2019/09/09 17:42:14
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    在一个长度为n的数组里的所有数字都在0到n-1的范围内。
    数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
    请找出数组中任意一个重复的数字。
    例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
'''


# here put the import lib
def duplicate(nums,duplication):
    if not nums or len(nums) <= 0:
        return False
    
    n = len(nums)
    for i in nums:
        if i < 0 or i >= n:
            return False
    for i in range(n):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                duplication[0] = nums[i]
                return True
            else:
                index = nums[i]
                nums[i],nums[index] = nums[index],nums[i]
    return False