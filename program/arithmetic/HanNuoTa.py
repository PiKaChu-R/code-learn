#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Han.py
    @Time    :   2019/06/21 11:27:50
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   汉诺塔问题，分治算法
'''

'''
1.将a上的前n-1个挪到b上；
2.将a上的最后一个挪到c上；
3.将b上的n-1个挪到c上，完成。
'''


# here put the import lib

k = 0


def move(n, a, buffe, c):
    if n == 1:
        print(a, '-->', c) # 当a上只有1个的时候，挪到c上，完成
        global k
        k += 1
    else:
        move(n-1, a, c, buffe) # 实现 1
        move(1, a, buffe, c)   # 实现 2
        move(n-1, buffe, a, c) # 实现 3


move(3, 'a', 'b', 'c')
print(k)
