#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Test2.py
    @Time    :   2019/09/07 19:36:45
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    华为笔试第二题：
    一个矩阵，5*5，取相邻（二个成员有一个边是相同的）的6个，输入一个6个成员列表，判断是否满足？矩阵成员如下：
    [[1,2,3,4,5],
    [11,12,13,14,15],
    [21,22,23,24,25],
    [31,32,33,34,35],
    [41,42,43,44,45]].
    
    输入描述：
    包含6个矩阵成员数组，如：1，2，3，4，5，11以一个空格分隔，支持多行
    1，2，3，4，5，11
    1，2，11，14，25，15
    
    输出描述：
    满足输出1，否则输出0，每一行输入一个输出
    1
    0
    
    备注：
    输入没有合法判断，每个成员不重复。
'''


# here put the import lib
import sys


def getPosition(num):
    if num <= 5:
        return (0, num-1)
    if 11 <= num <= 15:
        return (1, num % 10-1)
    if 21 <= num <= 25:
        return (2, num % 10-1)
    if 31 <= num <= 35:
        return (3, num % 10-1)
    if 41 <= num <= 45:
        return (4, num % 10-1)
    return -1


def main_1():
    for line in sys.stdin:
        nums = list(map(int, line.split()))
        flag = True
        pre = getPosition(nums[0])
        if pre == -1:
            print('0')
            continue
        for i in range(1, len(nums)):
            now = getPosition(nums[i])
            if abs(pre[0]+pre[1]-now[0]-now[1]) == 1:
                pre = now
                continue
            if abs(pre[0]-now[0]) == 1 and abs(pre[1]-now[1]) == 4:
                pre = now
                continue
            else:
                flag = False
                break
        if flag:
            print('1')
        else:
            print('0')


def main_2():
    for line in sys.stdin:
        nums = list(map(int, line.split()))
        if len(nums) != 6:
            print('0')
            continue
        ans = 0
        for i in range(1, len(nums)):
            a, b = divmod(nums[i], 10)
            if a in [0, 1, 2, 3, 4] and b in [1, 2, 3, 4, 5]:
                tmp = abs(nums[i]-nums[i-1])
                if tmp in [1, 6, 10, 40]:
                    ans += 1
            else:
                break
        if ans == 5:
            print('1')
        else:
            print('0')


def findRoot(T, x):
    if T[x] == -1:
        return x
    tmp = findRoot(T, T[x])
    T[x] = tmp
    return tmp

# 使用并查集，设置大小为6的并查集，其中每个成员单独成组，判断两两是否相邻，若相邻则合并为一组，最后判断是否存在孤立的组，有输出0，无输出1.
def main_3():
    for line in sys.stdin:
        nums = list(map(int, line.split()))
        Tree = [-1] * 6
        for i in range(6):
            for j in range(i+1, 6):
                x = max(nums[i], nums[j])
                y = min(nums[i], nums[j])
                if x-y == 1 or x-y == 10:
                    a = findRoot(Tree, i)
                    b = findRoot(Tree, j)
                    if a != b:
                        Tree[a] = b
        if Tree.count(-1) == 1:
            ans = 1
        else:
            ans = 0
        print(ans)


if __name__ == "__main__":
    main_3()
