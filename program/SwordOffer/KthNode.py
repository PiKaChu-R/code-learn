#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   KthNode.py
    @Time    :   2019/09/16 16:24:13
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    给定一颗二叉搜索树，请找出其中的第k大的结点。例如，
         5
        / \
        3  7
        /\ /\
        2 4 6 8 中，
    按结点数值大小顺序第三个结点的值为4。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def KthNode(self, pRoot, k):
        if not pRoot or not k:
            return None

        stack = []

        def helper(root):

            if not root:
                return
            if root.left:
                helper(root.left)
            stack.append(root)
            if root.right:
                helper(root.right)

        helper(pRoot)
        if k > len(stack):
            return None
        return stack[k-1]

    def KthNode2(self, pRoot, k):
        if k <= 0 or not pRoot:
            return None
        treeStack, nodesQue = [], []
        pNode = pRoot
        while pNode or treeStack:
            while pNode:
                treeStack.append(pNode)
                pNode = pNode.left
            if treeStack:
                pNode = treeStack.pop()
                nodesQue.append(pNode.val)
                pNode = pNode.right
        if k > len(nodesQue):
            return None
        return nodesQue[k-1]
