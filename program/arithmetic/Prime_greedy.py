#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Prime_greedy.py
    @Time    :   2019/06/21 16:46:27
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   Prime ，贪心
'''

'''
100=0
'''


# here put the import lib
import numpy as np
# 数据结构
c = [[100, 23, 100, 100, 100, 28, 36],
	 [23, 100, 20, 100, 100, 100, 1],
	 [100, 20, 100, 15, 100, 100, 4],
	 [100, 100, 15, 100, 3, 100, 9],
	 [100, 100, 100, 3, 100, 17, 16],
	 [28, 100, 100, 100, 17, 100, 25],
	 [36, 1, 4, 9, 16, 25, 100]]

# 初始化
u = [0]
v_u = [1, 2, 3, 4, 5, 6]
closet = [0] * len(c)
lowcost = c[0]
s = [1] * len(c)
s[0] = 100
while len(v_u) > 1:
	# 找最小
	node = lowcost.index(min(np.multiply(np.array(lowcost),np.array(s))))
	s[node] = 100  # 表示该节点已加入u
	# 将节点加入到u中，并从v_u中删除
	u.append(node)
	v_u.remove(node)
	# 更新closet和lowcost列表
	for n in v_u:
		if c[n][node]<lowcost[n]:
			lowcost[n] = c[n][node]
			closet[n] = node
print(closet)
print(lowcost)
