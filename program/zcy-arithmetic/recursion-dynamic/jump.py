#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   jump.py
    @Time    :   2019/09/04 16:47:30
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    跳跃游戏
'''


# here put the import lib

# 数组长度为n，要求时间O(n)，空间O(1).

def jump(arr):
    if arr == None or len(arr) == 0:
        return 0

    jump = 0
    cur = 0
    _next = 0

    for i in range(len(arr)):
        if cur <i:
            jump += 1
            cur = _next
        _next = max(_next,i+arr[i])
    
    return jump
arr = [3,2,3,1,1,4]
print(jump(arr))