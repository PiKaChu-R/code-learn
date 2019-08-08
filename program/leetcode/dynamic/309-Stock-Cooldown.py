#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Stock-Cooldown.py
    @Time    :   2019/08/08 21:26:10
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   121
'''

'''
309.最佳股票买卖时机含有冷冻期：给定一个整数数组，
    其中第 i 个元素代表了第 i 天的股票价格 。
    设计一个算法计算出最大利润。在满足以下约束条件下，
    你可以尽可能地完成更多的交易（多次买卖一支股票）: 
    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。


'''


# here put the import lib



class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = 0
        dp_pre_0 = 0
        
        for i in range(n):
            if i == 0:
                # 第1天因为没有卖出，所以dp_i_0 = 0,假如买入的话，dp_i_1 = -prices[i]，此时收益dp_pre_0 = 0
                dp_i_0 = 0
                dp_i_1 = -prices[i]
                dp_pre_0 = 0
                continue
                
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = tmp
        
        return max(dp_i_0,0)