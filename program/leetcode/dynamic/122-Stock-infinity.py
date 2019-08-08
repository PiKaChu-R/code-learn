#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Stock-infinity.py
    @Time    :   2019/08/08 21:26:10
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   121
'''

'''
122.买卖股票的最佳时机II：设计一个算法来计算你所能获取的最大利润。
    你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


'''


# here put the import lib

class Solution:
    def maxProfit(self, prices):
        
        if not prices:
            return 0
        
        res = 0
        
        for i in range(1,len(prices)):
            res += max(0,prices[i]-prices[i-1])
        return res

    def maxProfit(self, prices):
            # 动态规划
            if not prices: return 0
            buy = -prices[0]
            sell = 0
            for p in prices[1:]:
                buy = max(buy, sell - p)
                sell = max(sell, p + buy)
            return sell