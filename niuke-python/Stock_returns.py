#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Stock_returns.py
    @Time    :   2019/04/22 17:17:13
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入
    第一行为天数n
    接下来n行 为数组的n个整数元素，代表第n天该股票的价格
    输出
    输出为b，s      #代表第b天买入，第s天卖出
    天数从0开始
    如果没有适合的买入卖出输出-1,-1
    同样收益时越晚买入越早卖出更符合需要
    样例输入
    5
    2
    1
    4
    5
    3
    样例输出
    1, 3
'''


# here put the import lib

if __name__ == "__main__":
    
    k = int(input())
    price = []
    
    for i in range(k):
        x = int(input())
        price.append(x)

    # print(price)
    max_price = 0
    position_s = -1
    position_e = -1

    for i in range(len(price)):
        for j in range(i,len(price)):
            if max_price < (price[j] - price[i]):
                max_price = price[j] - price[i]
                position_s = i
                position_e = j
            elif max_price == (price[j] - price[i]):
                if position_s < i:
                    position_s = i
                if position_e > j:
                    position_e = j
    

    print(position_s,position_e,max_price)