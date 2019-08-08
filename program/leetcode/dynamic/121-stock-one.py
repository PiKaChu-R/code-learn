#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Stock-One.py
    @Time    :   2019/08/08 21:26:10
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   121
'''

'''
121.买卖股票的最佳时机：如果你最多只允许完成一笔交易（即买入和卖出一支股票），
    设计一个算法来计算你所能获取的最大利润。注意你不能在买入股票前卖出股票。

'''


# here put the import lib



class Solution:
    def maxProfit(self, prices)：
        # 采用动态规划—自顶向下
        if not prices:
            return 0
        
        # dp = [0]*len(prices)
        # dp[0] = prices[0]
        max_price = 0
        min_price = prices[0]
        
        for i in range(1,len(prices)):
            if prices[i] <= min_price:
                min_price = prices[i]
                continue
            max_price = max(prices[i] - min_price, max_price)
        return max_price