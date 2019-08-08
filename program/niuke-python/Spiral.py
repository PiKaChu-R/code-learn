#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Spiral.py
    @Time    :   2019/04/22 16:49:28
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   无法实现螺旋部分。参考2程序，
                 与之前相似程序实现方法相似Spiral_number.py
'''

'''
编程输出以下格式的数据。
when i=1:
1 
4   5   2
3
when i=2:
1   2 
8   9  10   3
7  12 11  4
6   5
'''


# here put the import lib

import os
import sys


def luoxuan(key):
    # print 'IN'
    hang = 2 + key
    set_list = {}
    for i in range(hang):
        set_list[i] = []
        if i == 0:
            for j in range(key):
                set_list[i].append(j+1)
        elif i == (hang-1):
            for j in range(key):
                set_list[i].append(key*3-j)
        elif i == 1:
            for j in range(key+2):
                if j != (key + 1):
                    set_list[i].append(key*4+j)
                else:
                    set_list[i].append(set_list[0][-1]+1)
        else:
            # k = set_list[i-1]
            # print (k)
            for j in range(key+2):
                if j == 0:
                    set_list[i].append(set_list[i-1][0]-1)
                else:
                    set_list[i].append(set_list[i][j-1]-1)
        print(set_list, type(set_list[0]))


if __name__ == "__main__":
    key = int(input("The number:"))
    luoxuan(key)
