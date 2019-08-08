#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   bag_greedy.py
    @Time    :   2019/06/21 16:44:41
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   背包问题，贪心算法
'''

'''
物品可分割的装载问题称为背包问题，不可分割问题的装载问题称为0-1背包问题。
0-1背包问题不具有贪心选择性质，贪心算法不能得到全局最优解，仅仅是最优解的近似解。
0-1背包问题可用动态规划算法求解。
'''


# here put the import lib



# datas中每个元素代表一个古董，每个列表第一个元素代表古董重量，第二个元素代表古董价值
datas = [[4, 3], [2, 8], [9, 18], [5, 6], [5, 8], [8, 20], [5, 5], [4, 6], [5, 7], [5, 15]]
m = 30 # 毛驴运载能力
w = 0 # 获取的总价值
# 计算出每件宝物的性价比，按照从高到低排序
for i in range(len(datas)):
	price = datas[i][1] / datas[i][0]
	datas[i].append(price)  # 增加性价比
datas.sort(key=lambda data: data[2], reverse=True) # 按性价比排序
# 按性价比从大到小选取宝物，直到达到毛驴的运载能力
for data in datas:
	if data[0] <= m:
		w += data[1]
		m -= data[0]
	else:
		w += data[2] * m  # 取走宝物的一部分
		break
print('总价值：',w)
