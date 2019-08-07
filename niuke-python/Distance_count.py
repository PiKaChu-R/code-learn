#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Distance_count.py
    @Time    :   2019/04/17 17:42:50
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    定义两个大于2的偶数之间的距离，为这两个数之间质数的个数。从小到大输入n个大
    于2的偶数，输出所有数两两之间距离的总和（应该有n*(n-1)/2个距离，输出总和就好)。
    输入
    第一行是输入偶数的个数，最小为2，最大可能到几万。之后每行为一个偶数，最小是4，
    最大可能是几百万，不重复的升序排列。
    输出
    输入数据两两间距离的总和，这应该是一个不小于0的整数。
    样例输入
    3
    4
    6
    12
    样例输出
    6
'''

""" 
    python 判断素数的两种方式
"""


# here put the import lib

import math

def distance_count(x, y):

    if (x > y):
        x, y = y, x
    return distance_zero_2(y) - distance_zero_2(x)


def distance_zero(a):

    count = 1
    for i in range(2, a):
        for j in range(2, i+1):
            if i % j == 0:
                # print('22222222222')
                break
            elif j == (i-1):
                # print ('1111112222222')
                count = count+ 1
                break
    # print (count)
    return count

def distance_zero_2(a):

    count = 0

    for i in range(a):
        sushu = True
        for j in range(2,int(math.sqrt(i))+1):
            if i % j ==0:
                sushu = False
                break
        if sushu:
            count += 1
    return count 

if __name__ == "__main__":
    num = int(input("The number of even:"))
    list_even = []
    for i in range(num):
        list_even.append(int(input("Even:")))

    print (list_even)

    sum_dis = 0
    for x in range(len(list_even)):
        for y in range(x+1,len(list_even)):
            k = distance_count(list_even[x], list_even[y])
            sum_dis += k

    print (sum_dis)