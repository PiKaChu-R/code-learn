#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   994-Bad-Orange.py
    @Time    :   2019/08/11 21:25:54
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
在给定的网格中，每个单元格可以有以下三个值之一：
    值 0 代表空单元格；值 1 代表新鲜橘子；值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
'''


# here put the import lib
class Solution:
    def orangesRotting(self, grid):
        
        if not grid or any(grid) != 1:
            return 0
        
        import collections
        q= collections.deque()        
        n = len(grid)
        m = len(grid[0])
        
        # 记录所有的初始坏橘子
        for r,row in enumerate(grid):
            for c,col in enumerate(row):
                if col == 2:
                    q.append((r,c,0))
        
        # 对坏橘子周围的位置进行遍历，并判断
        # yield 能够保持最后一次调用的值。
        def bfs(i,j):
            for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                tmp_x = x + i
                tmp_y = y + j
               
                if 0 <= tmp_x < n and 0 <= tmp_y < m :
                    yield tmp_x,tmp_y
        
        # 对所有的坏橘子进行遍历，并计算每个橘子坏的时间（根据其父橘子） 
        d = 0
        while q:
            r,c,d = q.popleft()
            for i,j in bfs(r,c):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    q.append((i,j,d+1))
        
        if any(1 in row for row in grid):
            return -1
        return d
        # return -1 if any(grid) == 1 else d