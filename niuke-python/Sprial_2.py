#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Sprial_2.py
    @Time    :   2019/04/22 17:09:47
    @Author  :   R.
    @Version :   2.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    Sprial.py:可实现方法
'''


# here put the import lib
import itertools


def spiral(init):
    status = itertools.cycle(['right', 'down', 'left', 'up'])  # 用于状态周期性的切换
    movemap = {
        'right': (1, 0),
        'down': (0, 1),
        'left': (-1, 0),
        'up': (0, -1),
    }
    # 初始化二维数组
    position_map = dict.fromkeys(
        [(x, y) for x in range(init) for y in range(init)])
    # 初始化当前位置以及当前方向
    positon = (0, 0)
    new_status = next(status)
    for i in range(4*init+1, init * (init+4) + 1):
        old_positon = positon
        # print(list( zip(positon, movemap[new_status])))
        # print('22')
        # print(list(map(sum, zip(positon, movemap[new_status]))))

        # 根据状态进行移动
        positon = tuple(map(sum, zip(positon, movemap[new_status])))
        # 如果超过范围或者碰到已经有值的位置则切换方向
        if (positon not in position_map) or (position_map[positon]):
            new_status = next(status)

            positon = tuple(map(sum, zip(old_positon, movemap[new_status])))

        position_map[old_positon] = i

    # 构造输出信息
    print("When:init = {}".format(init))

    # 打印第一行
    for i in range(1, init+1):
        if i < init:
            print("{}".format(i), end='\t')
        else:
            print("{}".format(i))

    # 构造中心螺旋结构
    for i in range(init):
        print("{}".format(4 * init - i), end='\t')
        for j in range(init):

            print((str(position_map[(j, i)])), end='\t')
        print("{}".format(i + init + 1))

    # 添加最后一行
    for i in range(init*3, init*2, -1):
        # 打印第一行
        print("{}".format(i), end='\t')
        if i == init:
            print("{}".format(i))


if __name__ == "__main__":
    # 参数为init值
    spiral(3)
