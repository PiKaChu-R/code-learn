#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   2-sum.py
    @Time    :   2019/06/05 11:15:32
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
'''


# here put the import lib

class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            temp = target - nums[i]
            if (temp in nums) and nums.index(temp) != i:
                return i, nums.index(temp)

if __name__ == "__main__":
    nums = list(map(int, input("").split()))
    target = int(input(""))
    solution = Solution()
    k1,k2 = solution.twoSum(nums,target)
    print(k1,k2)