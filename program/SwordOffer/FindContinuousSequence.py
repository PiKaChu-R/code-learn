#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   FindContinuousSequence.py
    @Time    :   2019/09/09 16:48:49
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    找出所有和为S的连续正数序列
    输出所有和为S的连续正数序列。序列内按照从小至大的顺序，
    序列间按照开始数字从小到大的顺序
'''


# here put the import lib
def FindContinuousSequence(tsum):
    if tsum < 3:
        return []
    small, big = 1, 2
    middle = (tsum+1)//2
    curSum = small + big
    ans = []
    while small < middle:
        if curSum == tsum:
            ans.append(list(range(small,big+1)))
            big += 1
            curSum += big
        elif curSum > tsum:
            curSum -= small
            small += 1
        else:
            big += 1
            curSum += big
    return ans