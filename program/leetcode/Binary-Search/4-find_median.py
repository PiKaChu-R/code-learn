#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   find_median.py
    @Time    :   2019/06/10 20:33:43
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   二分查找， 没太看懂
'''

'''
定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

'''


# here put the import lib
import numpy
import math


def findMedian(s1, s2):
    # 时间复杂度不为O(log(m+n))
    s1 = s1 + s2
    s1.sort()
    k = math.ceil(len(s1)/2)-1
    if (len(s1) % 2) == 0:
        val = (s1[k]+s1[k+1])/2
    else:
        val = s1[k]
    print(k, s1, val)


def findMedian2(s1, s2):

    n1 = len(s1)
    n2 = len(s2)
    if n1 > n2:
        return findMedian2(s2, s1)

    k = (n1+n2+1)//2
    left = 0
    right = n1
    while left < right:
        m1 = left+(right-left)//2
        m2 = k-m1
        if s1[m1] < s2[m2-1]:
            left = m1+1
        else:
            right = m1
    m1 = left 
    m2 = k -m1
    c1 = max(s1[m1-1] if m1 > 0 else float("-inf"), s2[m2-1] if m2 > 0 else float("-inf") )
    if (n1 + n2) % 2 == 1:
        return c1
    c2 = min(s1[m1] if m1 < n1 else float("inf"), s2[m2] if m2 <n2 else float("inf"))
    print (m1,m2)
    return (c1 + c2) / 2



if __name__ == "__main__":
    # s1 = numpy.array([1,3])
    s1 = [-1,1,3,5,7,9]
    # s2 = numpy.array([2,4])
    s2 = [2,4,6,8,10,12,14,16]
    k = findMedian2(s1, s2)
    print(k)

    