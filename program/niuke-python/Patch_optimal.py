#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Patch_optimal.py
    @Time    :   2019/04/20 15:00:01
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    题目描述：游戏网站提供若干升级补丁，每个补丁大小不一，玩家要升级到最新版，
    如何选择下载哪些补丁下载量最小。
    输入：
    第一行输入                第一个数为用户版本 第二个数为最新版本，空格分开
    接着输入N行补丁数据       第一个数补丁开始版本 第二个数为补丁结束版本 第三个数为补丁大小，空格分开
    输出：
    对于每个测试实例，输出一个升级路径以及最后实际升级的大小
    样例输入：
    1000 1050
    1000 1020 50
    1000 1030 70
    1020 1030 15
    1020 1040 30
    1030 1050 40
    1040 1050 20
    样例输出：
    1000->1020->1040->1050(100)
'''


# here put the import lib


def dijkstra(s, costs):
    point_list = []
    point_list.append(s[0])
    for i in range(len(costs)):
        if not costs[i][1] in point_list:
            point_list.append(costs[i][1])
    distence = [float('inf') for _ in range(len(point_list))]
    used = [False for _ in range(len(point_list))]
    cost_l = [[float('inf') for _ in range(V)] for _ in range(V)]
    distence[s[0]] = 0
    while True:
        v = -1
        for u in range(len(point_list)):
            if not used[u] and (v == -1 or distence[u] < distence[v]):
                v = u
        if v == -1:
            break

        used[v] = True
        costs_m = []
        
        for u in range(len(point_list)):
            distence[u] = min(distence[u], distence[v])
    print(distence, point_list)


if __name__ == "__main__":
    start_end = list(map(int, input().split()))
    k = ''
    Path_list = []
    while True:
        k = list(map(int, input().split()))
        # print (k)
        if k[0] == 0 or k[0] == "":
            break
        Path_list.append(k)

    dijkstra(start_end, Path_list)

    # print("Exit",Path_list)
