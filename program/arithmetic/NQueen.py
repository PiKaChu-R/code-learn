#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   NQueen.py
    @Time    :   2019/07/15 19:36:12
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    N皇后问题返回题解
'''


# here put the import lib
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def could_place(row,col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
        def place_queen(row,col):
            queens.add((row,col))
            cols[col]=1
            hill_diagonals[row - col]=1
            dale_diagonals[row + col]=1
        
        def remove_queen(row,col):
            queens.remove((row,col))
            cols[col]=0
            hill_diagonals[row - col]=0
            dale_diagonals[row + col]=0
        
        def add_solution():
            solution = []
            for _,col in sorted(queens):
                solution.append('.' * col + 'Q' + '.'*(n-col-1))
            output.append(solution)
        
        def backtrack(row = 0):
            for col in range(n):
                if could_place(row,col):
                    place_queen(row,col)
                    if row +1 ==n:
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row,col)
        
        cols = [0]*n
        hill_diagonals = [0]*(2*n-1)
        dale_diagonals = [0]*(2*n-1)
        queens = set()
        output = []
        backtrack()
        return output