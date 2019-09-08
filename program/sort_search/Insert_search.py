#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Insert_search.py
    @Time    :   2019/06/24 14:47:36
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   插值查找
'''

'''
在有序数组中使用，和二分查找相似，是二分查找的改进
插值查找是根据要查找的关键字key与查找表中最大最小记录的关键字比较后的 
查找方法，其核心就在于插值的计算公式 (key-a[low])/(a[high]-a[low])*(high-low)。
时间复杂度o(logn)但对于表长较大而关键字分布比较均匀的查找表来说，效率较高,在最坏的情况下可能需要 O（n）.
空间复杂度：O（1）.
'''


# here put the import lib


def Insert_search(seq,key):
    low = 0
    high = len(seq)-1
    time = 0
    while low < high:
        time += 1
        mid = low + (key-seq[low])//(seq[high]-seq[low])*(high-low)
        print("mid=%s, low=%s, high=%s" % (mid, low, high))
        if key < seq[mid]:
            high = mid -1
        elif key > seq[mid]:
            low = mid + 1
        else:
            print('time:%s'%time)
            return mid
    print('time:%s'%time)
    return 0


if __name__ == "__main__":
    seq = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    # seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
    result = Insert_search(seq, 15)
    print(result)