#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   maxInWindows.py
    @Time    :   2019/09/16 17:12:59
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
    例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
    他们的最大值分别为{4,4,6,6,6,5}；
    针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
    {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''


# here put the import lib
class Solution:
    def maxInWindows(self, num, size):
        if not num or size <= 0 or size > len(num):
            return []
        left = 0
        right = size - 1
        ans = []
        while right < len(num):
            ans.append(max(num[left:right+1]))
            left += 1
            right += 1
        return ans

    def maxInWindows2(self, num, size):
        if not num or size <= 0 or size > len(num):
            return []
        length = len(num)
        curnum = max(num[:size])
        ans = [curnum]
        for i in range(0, length-size):
            if num[i] == curnum:
                curnum = max(num[i+1:i+1+size])
            elif num[i+size] > curnum:
                curnum = num[i+size]
            ans.append(curnum)
        return ans
