#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   bubbleSort.py
    @Time    :   2019/06/21 17:59:02
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   冒泡排序
'''

'''
'''


# here put the import lib
import sys

def bubbleSort(seq):
    assert (type(seq)==type(['']))
    n = len(seq)
    if n<=1:
        return seq
    
    for i in range(n-1):
        for j in range(n-1-i):
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]
    
    return seq

def bubble_Sort(seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]):
    # 优化后
    print(seq,type(seq))
    n = len(seq)
    for i in range(n-1):
        isSorted = True
        for j in range(n-1-i):
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]
                isSorted = False
        if isSorted:
            break
    return seq

seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
print(bubbleSort(seq)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]