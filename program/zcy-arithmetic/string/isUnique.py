#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   isUnique.py
    @Time    :   2019/09/12 20:12:24
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    字符数组中是否所有的字符都只出现过一次。
'''


# here put the import lib

# 时间复杂度为O(n)，空间复杂度为O(n)
def isUnique1(s):
    if s == None:
        return True
    d = dict()
    for i in range(len(s)):
        if s[i] in d:
            return False
        d[i] = True
    return True


# 要求实现空间复杂度为O(1)的实现。
def isUnique2(s):
    if not s:
        return True
    heapSort(s)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False
    return True

# 实现非递归的堆排序


def heapSort(s):
    for i in range(len(s)//2-1, -1, -1):
        heapInsert(s, i, len(s)-1)

    for i in range(len(s)-1, 0, -1):
        s[0], s[i] = s[i], s[0]
        heapInsert(s, 0, i-1)


def heapInsert(s, start, end):
    root = start
    while True:
        child = 2*root + 1
        if child > end:
            break
        if child + 1 <= end and s[child] > s[child+1]:
            child += 1
        if s[root] > s[child]:
            s[root], s[child] = s[child], s[root]
            root = child
        else:
            break


s = ['a', 'b', 'e', 'a']

print(isUnique2(s))
