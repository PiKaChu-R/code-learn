#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   reOrderArray.py
    @Time    :   2019/09/09 10:27:07
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
    使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
    并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


# here put the import lib
def reOrderArray(array):
    # 奇数偶数内部有序
    if not array:
        return []
    
    odd = []
    even = []
    for i in array:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    return odd+even

def reOrderArray2(array):
    # 内部未有序
    if not array:
        return []
    i = 0
    j = len(array)-1
    while i <= j:
        while array[i]%2 != 0:
            i += 1
        while array[j]%2 == 0:
            j -= 1
        if i <= j:
            array[i],array[j] = array[j],array[i]
        i += 1
        j -= 1
    return array