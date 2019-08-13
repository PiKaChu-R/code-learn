#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   200-NumofIsland.py
    @Time    :   2019/08/12 20:17:25
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   bfs
'''

'''
    给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
    一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
    你可以假设网格的四个边均被水包围。
'''


# here put the import lib

from collections import deque
class Solution:
    def numIslands(self, grid):
        
        if not grid:
            return 0

        
        dis = [(-1,0),(1,0),(0,1),(0,-1)]
        count = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == '1':
                    count += 1
                    visited[i][j] = True
                    q = deque()
                    q.append((i,j))
                    while q:
                        a,b = q.popleft()
                        for x,y in dis:
                            tmp_x = a+x
                            tmp_y = b+y
                            if 0 <= tmp_x < row and 0 <= tmp_y < col and not visited[tmp_x][tmp_y] and grid[tmp_x][tmp_y] == '1':
                                q.append((tmp_x,tmp_y))
                                visited[tmp_x][tmp_y] = True

so = Solution()
k = so.numIslands(3,7)
print(k)
