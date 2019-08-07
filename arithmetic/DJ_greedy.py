#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   DJ_greedy.py
    @Time    :   2019/06/21 15:34:04
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   迪杰特斯拉算法
'''

'''
Dijkstra算法主要针对的是有向图的单元最短路径问题，且不能出现权值为负的情况！
Dijkstra算法类似于贪心算法，其应用根本在于最短路径的最优子结构性质。
'''


# here put the import lib
MAX_value = 999999

def dijkstra(graph, s):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    dist = [MAX_value] * len(graph)
    dist[s] = 0  # 记录最终的到各个点的最短路径长度
    S = []  # 已经走过的节点
    Q = [i for i in range(len(graph))]  # 记录有多少个节点
    dist_init = [i for i in graph[s]]  # 初始时的路线
    while Q:
        u_dist = {v: d for v, d in enumerate(dist_init) if v in Q}
        u = min(u_dist, key=u_dist.get)
        # print(u,dist_init)
        S.append(u)
        Q.remove(u)

        for v, d in enumerate(graph[u]):
            if 0 < d < MAX_value:
                if dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
                    dist_init[v] = dist[v]
    return dist


if __name__ == '__main__':
    graph_list = [[0, 9, MAX_value, MAX_value, MAX_value, 14, 15, MAX_value],
                  [9, 0, 24, MAX_value, MAX_value, MAX_value, MAX_value, MAX_value],
                  [MAX_value, 24, 0, 6, 2, 18, MAX_value, 19],
                  [MAX_value, MAX_value, 6, 0, 11, MAX_value, MAX_value, 6],
                  [MAX_value, MAX_value, 2, 11, 0, 30, 20, 16],
                  [14, MAX_value, 18, MAX_value, 30, 0, 5, MAX_value],
                  [15, MAX_value, MAX_value, MAX_value, 20, 5, 0, 44],
                  [MAX_value, MAX_value, 19, 6, 16, MAX_value, 44, 0]]

    distance = dijkstra(graph_list, 0)
    print(distance)
