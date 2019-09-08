#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   quicksort.py
    @Time    :   2019/06/21 17:38:20
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   快速排序
'''

'''
'''


# here put the import lib

def partition(seq):
    pi = seq[0]

    lo = [x for x in seq[1:] if x <= pi]
    hi = [x for x in seq[1:] if x > pi]
    return lo, pi, hi


def quicksort(seq):
    if len(seq) <= 1:
        return seq

    lo, pi, hi = partition(seq)

    return quicksort(lo) + [pi] + quicksort(hi)


def quicksort2(seq):
    if not seq:
        return []

    n = len(seq)
    mid_int = min(max(seq[0], seq[n//2]), max(seq[n//2],seq[-1]))
    index = seq.index(mid_int)
    lo = quicksort2([x for x in (seq[:index]+seq[index+1:])if x <= mid_int])
    hi = quicksort2([x for x in (seq[:index]+seq[index+1:])if x > mid_int])

    return lo+[mid_int]+hi

def quicksort3(seq):
    if not seq or len(seq) == 1:
        return seq

    def helper(left,right):
        if left >= right:
            return 
        low = left
        high = right
        key = seq[low]
        while left < right:
            while left < right and seq[right] > key:
                right -= 1
            seq[left] = seq[right]
            while left < right and seq[left] <= key:
                left += 1
            seq[right] = seq[left]
        
        seq[right] = key
        helper(low,left-1)
        helper(left+1,high)
    
    helper(0,len(seq)-1)
    return seq


seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
# print(quicksort2(seq))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(quicksort3(seq))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(seq)
