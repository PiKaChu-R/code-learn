#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   hanoi.py
    @Time    :   2019/08/30 20:06:49
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    汉诺塔问题，打印移动轨迹,最优过程：
    1.1~i-1移动到中间
    2.i移动到最右
    3.1~i-1移动到最右
    进阶问题：
        判断当前位置顺序是否在最优路径中,不在返回-1，在返回步骤几或者步骤数。
        步骤数：S(i)= 2^(i-1).
'''


# here put the import lib

def hanoi(n):
    if n > 0:
        solution(n, 'left', 'mid', 'right')


def solution(n, start, mid, to):
    if n == 1:
        print('move from '+start+ ' to '+ to)
    else:
        solution(n-1, start, to, mid)
        solution(1, start, mid, to)
        solution(n-1, mid, start, to)


def step2(arr):
    if len(arr) == 0:
        return -1
    start = 1
    mid = 2
    to = 3
    i = len(arr)-1
    res = 0
    tmp = 0
    while i >= 0:
        if arr[i] != start and arr[i] != to:
            return -1
        if arr[i] == to:
            res += 1 << i
            tmp = start
            start = mid
        else:
            tmp = to
            to = mid
        mid = tmp
        i -= 1
    return res


print(hanoi(5))
print(step2([3,3,2,1]))
