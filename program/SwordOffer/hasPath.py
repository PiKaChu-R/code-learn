#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   hasPath.py
    @Time    :   2019/09/16 17:44:51
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
    如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
    例如 [[a b c e], [s f c s], [a d e e]] 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
    因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''


# here put the import lib
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False
        temp = [list(matrix[i:i+cols]) for i in range(0, len(matrix), cols)]

        def helper(i, j, index, visited):
            if index == len(path):
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tmp_x = i+x
                tmp_y = j+y
                if 0 <= tmp_x < rows and 0 <= tmp_y < cols and (tmp_x, tmp_y) not in visited and temp[tmp_x][tmp_y] == path[index]:
                    visited.add((tmp_x, tmp_y))
                    if helper(tmp_x, tmp_y,  index+1, visited):
                        return True
                    visited.remove((tmp_x, tmp_y))
            return False

        for i in range(rows):
            for j in range(cols):
                if temp[i][j] == path[0] and helper(i, j, 1, {(i, j)}):
                    return True
        return False