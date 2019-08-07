#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Sort_num.py
    @Time    :   2019/04/19 17:12:33
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    从键盘接收若干个整数（直接输入回车表示结束），用冒泡法或选择法进行排序
    （从小到大），并将排序结果在屏幕上输出。同时估计算法的复杂度。

    两个算法的时间复杂度都是O(n^2)
'''


# here put the import lib

def Bubble_sort(num):

    for i in range(len(num)-1):
        for j in range(len(num)-1, i, -1):
            if num[j-1] > num[j]:
                num[j-1], num[j] = num[j], num[j-1]

    print(num)


def Selection_sort(num):

    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if num[i] > num[j]:
                num[i], num[j] = num[j].num[i]

    print(num)


if __name__ == "__main__":

    num = []
    k = input().strip().split()
    for i in range(len(k)):
        num.append(int(k[i]))

    Bubble_sort(num)  # 冒泡排序
    Selection_sort(num) # 选择排序
