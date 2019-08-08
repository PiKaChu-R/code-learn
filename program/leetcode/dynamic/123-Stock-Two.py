#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Stock-Two.py
    @Time    :   2019/08/08 21:26:10
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   121
'''

'''
123.买卖股票的最佳时机III：设计一个算法来计算你所能获取的最大利润。
    你最多可以完成两笔交易。
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


'''


# here put the import lib



class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[0]*n for _  in range(3)]
        
        for i in range(1,3):
            pre_max = -prices[0]
            for j in range(1,n):
                pre_max = max(pre_max, dp[i-1][j-1]-prices[j])
                dp[i][j] = max(dp[i][j-1], prices[j]+pre_max)
        return dp[-1][-1]