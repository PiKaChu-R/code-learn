#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   GetUglyNumber_Solution.py
    @Time    :   2019/09/09 15:42:03
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，
    但14不是，因为它包含因子7。习惯上我们把1当做是第一个丑数。求按从小
    到大的顺序的第N个丑数。
'''


# here put the import lib
def GetUglyNumber_Solution(n):
    if not n :
        return 0

    dp = [1]*n
    curIndex = 1
    min2 = 0
    min3 = 0
    min5 = 0

    while curIndex < n:
        minnum = min(dp[min2]*2,dp[min3]*3,dp[min5]*5)
        dp.append(minnum)
        while dp[min2]*2 <= minnum:
            min2 += 1
        while dp[min3]*3 <= minnum:
            min3 += 1
        while dp[min5]*5 <= minnum:
            min5 += 1
        curIndex += 1
    return dp[-1]