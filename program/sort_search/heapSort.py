#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   heapSort.py
    @Time    :   2019/06/22 16:16:59
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   堆排序
'''

'''
'''


# here put the import lib
def heapSort(seq):
    assert(type(seq) == type(['']))
    n = len(seq)
    if n <= 1:
        return seq

    def sift_down(seq,start,end):
        root = start
        while True:
            child = 2*root +1
            if child >end:
                break
            if child+1<=end and seq[child]>seq[child+1]:
                # 先比较两个子节点大小，更小的那个与父节点比较
                child+=1
            if seq[root] > seq[child]:
                seq[root],seq[child] = seq[child],seq[root]
                root = child
            else:
                break

    for start in range((n-2)//2,-1,-1):
        sift_down(seq,start,n-1)
    print(seq)
    
    for end in range(n-1,0,-1):
        seq[0],seq[end] = seq[end],seq[0]
        sift_down(seq,0,end-1)
    return seq

seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
print(heapSort(seq)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]