#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   207-Course-Schedule.py
    @Time    :   2019/08/12 20:49:29
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   可以广度，可以深度
'''

'''
    现在你总共有 n 门课需要选，记为 0 到 n-1。
    在选修某些课程之前需要一些先修课程。 例如，
    想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
    给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？
'''


# here put the import lib

class Solution:
    # 广度优先搜索
    def canFinish(self, numCourses, prerequisites):
        
        classes = [0 for _ in range(numCourses)]
        need = [[] for _ in range(numCourses)]
        q = []
        
        for cur ,pre in prerequisites:
            classes[cur] += 1
            need[pre].append(cur)
        
        for i in range(numCourses):
            if not classes[i]:
                q.append(i)
                
        while q:
            tmp = q.pop()
            numCourses -= 1
            for j in need[tmp]:
                classes[j] -= 1
                if not classes[j]:
                    q.append(j)
        
        return not numCourses
    
    # 深度优先搜索
    def canFinish2(self, numCourses, prerequisites):
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True
        
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True


so = Solution()
k = so.canFinish(2,[1,0])
print(k)
