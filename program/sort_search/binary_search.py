#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   binary_search.py
    @Time    :   2019/06/22 17:44:04
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   二分查找
'''

'''
'''


# here put the import lib
def binary_search(seq , key):
    low = 0
    high = len(seq)-1
    # time = 0
    while low<high:
        # time+=1
        mid = (low+high)//2
        if key<seq[mid]:
            high = mid-1
        elif key > seq[mid]:
            low = mid+1
        else:
            # print("%d"%time)
            return mid,seq[mid]
    
    # print("1__%d"%time)
    return False

seq = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
result = binary_search(seq, 99)
print (result)