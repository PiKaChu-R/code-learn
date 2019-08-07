#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Sprial_number.py
    @Time    :   2019/04/22 15:45:51
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   没看懂，好好看
'''

'''
    When i=0
    1
    When i=1
    7   8   9
    6   1   2
    5   4   3
    When i=2
    21  22  23  24  25
    20    7    8    9  10
    19    6    1    2  11
    18    5    4    3  12
    17  16  15  14  13
'''


# here put the import lib
import itertools


def sprial(x):

    line = 2*x + 1

    status = itertools.cycle(['left', 'down', 'right', 'up'])
    movemap = {
        'right': (1, 0),
        'down': (0, 1),
        'left': (-1, 0),
        'up': (0, -1),
    }

    position_map = dict.fromkeys(
        [(x, y) for x in range(line) for y in range(line)])

    positon = (line-1, 0)
    new_status = next(status)
    # 从最大值开始
    for i in range(line * line, 0, -1):
        old_positon = positon
        positon = tuple(map(sum, zip(positon, movemap[new_status])))
        # 如果超过范围或者碰到已经有值的位置则切换方向
        if (positon not in position_map) or (position_map[positon]):
            new_status = next(status)
            positon = tuple(map(sum, zip(old_positon, movemap[new_status])))
        # 相当于自加
        position_map[old_positon] = i

    print("When init={}".format(x))
    for i in range(line):
        for j in range(line):
            print((position_map[(j, i)]), end='\t')
        print('\n')


if __name__ == "__main__":
    k = int(input())
    sprial(k)
