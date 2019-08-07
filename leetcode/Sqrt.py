#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Sqrt.py
    @Time    :   2019/07/16 20:06:22
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    可用牛顿法或者二分法，牛顿法如下
'''


# here put the import lib


class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
