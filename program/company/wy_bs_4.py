#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   wy_bs_4.py
    @Time    :   2019/08/03 17:23:52
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
'''


# here put the import lib
if __name__ == "__main__":
    n,q = map(int,input().split())
    nums = list(map(int,input().split()))
    for _ in range(q):
        k = int(input())
        m = max(nums)
        if k > m:
            print(0)
            continue
        count = 0
