#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   selectSort.py
    @Time    :   2019/06/22 15:45:26
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   选择排序
'''

'''
'''


# here put the import lib

def selectSort(seq):
    assert (type(seq) == type(['']))
    n = len(seq)
    if n <= 1:
        return seq

    def _max(s):
        largest = s
        for i in range(s, n):
            if seq[i] > seq[largest]:
                largest = i
        return largest

    for i in range(n):
        max_seq = _max(i)
        if i != max_seq:
            seq[i], seq[max_seq] = seq[max_seq], seq[i]
 
    return seq


seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
print(selectSort(seq))
