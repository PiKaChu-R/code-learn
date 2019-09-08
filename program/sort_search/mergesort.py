#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   mergesort.py
    @Time    :   2019/06/21 17:47:52
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   归并排序（二路）
'''

'''
'''


# here put the import lib

def mergesort(seq):
    
    mid = len(seq)//2
    left_seq ,right_seq = seq[:mid],seq[mid:]

    if len(left_seq)>1:
        left_seq = mergesort(left_seq)
    if len(right_seq)>1:
        right_seq = mergesort(right_seq)

    res = []
    while left_seq and right_seq:
        if left_seq[-1] < right_seq[-1]:
            res.append(left_seq.pop())
        else:
            res.append(right_seq.pop())
    res.reverse() # 反向排序
    return (left_seq or right_seq)+res

seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
print(mergesort(seq)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]