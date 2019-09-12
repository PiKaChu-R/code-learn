#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   getIndex.py
    @Time    :   2019/09/12 20:27:34
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    在有序但含有空格的数组中查找字符串,找到第一次出现的位置
'''


# here put the import lib
# 利用二分查找

def getIndex(s, target):
    if not s or not target:
        return -1
    res = -1
    left = 0
    right = len(s)-1
    while left <= right:
        mid = (left+right)//2
        if s[mid] == target:
            res = mid
            right = mid-1
        elif s[mid] != None:
            if s[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            i = mid
            while i >= left:
                if s[i] != None:
                    break
                i -= 1
            if i < left or s[i] < target:
                left = mid + 1
            else:
                if s[i] == target:
                    res = i
                right = i - 1
    return res


s = [None, 'a', None, 'a', None, 'b']
target = 'a'
print(getIndex(s, target))
