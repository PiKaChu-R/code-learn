#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   BinaySearch.py
    @Time    :   2019/09/08 21:05:26
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    二分查找的递归版本,迭代版本
'''


# here put the import lib
def BinarySearch(nums, target):
    # 迭代版本
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    while left <right:
        mid = left + (right-left)//2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    return -1


def BinarySearch2(seq,target,start,end):
    if start == end:
        return -1
    
    mid = (start+end)//2
    if target > seq[mid]:
        return BinarySearch2(seq,target,mid+1,end)
    elif target < seq[mid]:
        return BinarySearch2(seq,target,start,mid-1)
    else:
        return mid



seq = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
result1 = BinarySearch(seq, 99)
result2 = BinarySearch2(seq, 99,0,len(seq)-1)
print(result1)
print(result2)
