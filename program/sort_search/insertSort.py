#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   insertSort.py
    @Time    :   2019/06/22 16:00:40
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   插入排序
'''

'''
'''


# here put the import lib

def insertSort(seq):
    assert (type(seq) == type([""]))
    n = len(seq)
    if n <= 1:
        return seq

    for i in range(1, n):
        value = seq[i]
        j = i-1
        while j >= 0 and seq[j] > value:
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = value

    return seq

seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
print(insertSort(seq)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]