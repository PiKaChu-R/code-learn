#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Krusal_greedy.py
    @Time    :   2019/06/21 16:52:56
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   Krusal，贪心
'''

'''
'''


# here put the import lib
c = [[100, 23, 100, 100, 100, 28, 36],
	 [23, 100, 20, 100, 100, 100, 1],
	 [100, 20, 100, 15, 100, 100, 4],
	 [100, 100, 15, 100, 3, 100, 9],
	 [100, 100, 100, 3, 100, 17, 16],
	 [28, 100, 100, 100, 17, 100, 25],
	 [36, 1, 4, 9, 16, 25, 100]]

# 初始化
edge = []  # 存储边
nodes = []  # 存储edge中每个边对应的两个节点
nodeset = {} # 存储孤立节点,key表示节点号，value是一个列表，存储所有与key节点联通的节点集合
for i in range(len(c[0])):
	for j in range(i, len(c[i])):
		if c[i][j] < 100:
			edge.append(c[i][j])
			nodes.append((i, j))
	nodeset[i] = [i]
print('原始数据中全部权值:', edge)
print('原始数据中两两连接的节点:', nodes, '\n')
# 生成树
edge_val = [] # 已选择的边
node_val = [] # 已选择边的两个节点
while len(edge_val)<len(c[0])-1:  # 判断选择的边数是否小于n-1
	index = edge.index(min(edge)) # 寻找最小边
	n = nodes[index]
	if n[0] not in nodeset[n[1]]:  # 说明两个节点不在同一集合中
		print('每步选择的两个节点:', (n[0], n[1]))
		l = nodeset[n[1]]
		for k in l:
			nodeset[k].extend(nodeset[n[0]])
		nodeset[n[0]].extend(nodeset[n[1]])
		edge_val.append(edge[index])
		node_val.append((n[0], n[1]))
	edge[index] = 100  # 相当于删除边index 
print('\n')
print('两节点之间的权值:',edge_val)
print('总权值:',sum(edge_val))
print('两两连接的节点',node_val)
