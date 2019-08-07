#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   DAU_count.py
    @Time    :   2019/04/22 16:32:26
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入格式
    每一行包含一个 uid，遇到 0 时认为输入结束。
    输入共包含 N+1 行，可认为是无序的。
    输出格式
    一个数字：去重后 uid 的数量 M。
    输入样例
    12933
    111111
    59220
    69433
    59220
    111111
    0
    输出样例
    4
    数据范围
    0 < uid < 2^63
    时间 < 1s, 内存 < 32MB
    对于 30% 的数据，0 < N < 100,000, 0 < M < 100,000
    对于 100% 的数据，0 < N < 1,000,000, 0 < M < 800,000
'''


# here put the import lib

if __name__ == "__main__":

    list_uid = []
    while True:
        k = int(input())
        # print (k,type(k))
        if k == 0 :
            break
        list_uid.append(k)

    set_uid = set(list_uid)
    print (len(set_uid))