#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   FindNumsAppearOnce.py
    @Time    :   2019/09/09 16:40:47
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   解法存在问题，需要修正
'''

'''
    一个整型数组里除了两个数字之外，其他的数字都出现了两次。
    请写程序找出这两个只出现一次的数字。
'''


# here put the import lib
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        res = []
        for i in array:
            if array.count(i) == 1:
                res.append(i)
        return res