#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   1039-MinimumScoreTriangulationofPolygon.py
    @Time    :   2019/08/10 16:32:05
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   多边形三角剖分的最低得分  动态规划
'''

'''
    给定 N，想象一个凸 N 边多边形，其顶点按顺时针顺序依次标记为 A[0], A[i], ..., 
    A[N-1].假设您将多边形剖分为 N-2 个三角形。对于每个三角形，该三角形的值是顶点
    标记的乘积，三角剖分的分数是进行三角剖分后所有 N-2 个三角形的值之和。
    返回多边形进行三角剖分后可以得到的最低分。
'''


# here put the import lib

class Solution:
    def minScoreTriangulation(self, A):
        
        n = len(A)
        
        dp = [[float('inf')] * n for _ in range(n)]
        # 求由第i个点往前找第j个点，与i能够组成的三角形的最小和。
        for i in range(n):
            for j in range(i-1,-1,-1):
                if i-j < 2:
                    dp[j][i] = 0
                else:
                    for k in range(j+1,i):
                        # 迭代公式
                        dp[j][i] = min(dp[j][i], A[i]*A[j]*A[k] + dp[j][k]+dp[k][i])
        
        return dp[0][n-1]


so = Solution()
k = so.minScoreTriangulation([31,26,33,21,40])
print(k)
