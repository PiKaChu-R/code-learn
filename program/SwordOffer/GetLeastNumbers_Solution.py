#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   GetLeastNumbers_Solution.py
    @Time    :   2019/09/09 15:03:48
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入n个整数，找出其中最小的K个数。
    例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''


# here put the import lib

def GetLeastNumbers_Solution(tinput,k):
    import heapq
    if tinput == None or len(tinput) < k or len(tinput) <=0 or k<=0:
        return []
    output = []
    for n in tinput:
        if len(output) < k:
            output.append(n)
        else:
            output = heapq.nlargest(k,output)
            if n >= output[0]:
                continue
            else:
                output[0] = n
    return sorted(output[::-1])

def TopK(nums,k):
    if not nums or len(nums) < k or k <=0 or len(nums) <=0:
        return []
    
    def sift_down(nums,start,end):
        root = start
        while True:
            child = root * 2 +1
            if child > end:
                break
            if child+1 <= end and nums[child] < nums[child+1]:
                child += 1
            if nums[child] > nums[root]:
                nums[root] ,nums[child] = nums[child],nums[root]
                root = child
            else:
                break

    nums_k = nums[:k]
    for i in range(k//2-1,-1,-1):
        sift_down(nums_k,i,k-1)
    
    for i in range(k,len(nums)):
        if nums[i] < nums_k[0]:
            nums_k[0] = nums[i]
            sift_down(nums_k,0,k-1)
    
    return nums_k