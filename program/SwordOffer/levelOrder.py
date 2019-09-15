#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   levelOrder.py
    @Time    :   2019/09/15 17:16:38
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, pRoot):
        if not pRoot:
            return []
        ans = []
        tmp = []
        stack = [pRoot]
        last = pRoot
        while stack:
            node = stack.pop(0)
            tmp.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if node == last:
                ans.append(tmp)
                tmp = []
                if stack:
                    last = stack[-1]
        return ans