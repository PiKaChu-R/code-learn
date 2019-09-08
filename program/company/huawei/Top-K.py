#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Top-K.py
    @Time    :   2019/09/08 19:18:25
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    Top-k问题：求第k大或第k小。
    小：建立大顶堆
    大：建立小顶堆
'''


# here put the import lib
import random


def HeapSort(data, k):
    # if not data or len(data) <= k:
    #     return None

    def sift_down(data_k, start, end):
        root = start
        while True:
            child = 2*root+1
            if child > end:
                break
            if child+1 <= end and data_k[child] > data_k[child+1]:
                child += 1
            if data_k[root] > data_k[child]:
                data_k[root], data_k[child] = data_k[child], data_k[root]
                root = child
            else:
                break

    data_k = data[:k]
    print(data_k, '1')
    for i in range((k-2)//2, -1, -1):
        sift_down(data_k, i, k-1)
    print(data_k, '2')
    for j in range(k, len(data)):
        if data[j] > data_k[0]:
            data_k[0] = data[j]
            sift_down(data_k, 0, k-1)
    print(data_k,'3')
    return data_k

# 构建小顶堆跳转
def sift(li, low, higt):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= higt:  # 情况2：i已经是最后一层
        if j + 1 <= higt and li[j + 1] < li[j]:  # 右孩子存在并且小于左孩子
            j += 1
        if tmp > li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break  # 情况1：j位置比tmp小
    li[i] = tmp


def top_k(li, k):
    heap = li[0:k]
    print(heap, 'h')
    # 建堆
    for i in range(k // 2 - 1, -1, -1):
        sift(heap, i, k - 1)
    print(heap, 'h2')
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    print(heap, 'h3')
    # 挨个输出
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


if __name__ == '__main__':
    data = [0, 8, 6, 2, 4, 9, 1, 4, 6]
    print(sorted(data))
    print(HeapSort(data, 6))
    li = [0, 8, 6, 2, 4, 9, 1, 4, 6]
    print(top_k(li, 6))
