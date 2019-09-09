#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   TreeDepth.py
    @Time    :   2019/09/09 16:28:27
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一棵二叉树，求该树的深度。
    从根结点到叶结点依次经过的结点
    （含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self,pRoot):
        if not pRoot:
            return 0
        r = pRoot
        if r.left == None and r.right == None:
            return 1
        count1 = 1
        count2 = 1
        if r.left:
            count1 += self.TreeDepth(r.left)
        if r.right:
            count2 += self.TreeDepth(r.right)
        return max(count1,count2)
    # 非递归算法，利用一个栈以及一个标志位栈
    def TreeDepth2(self, pRoot):
        if not pRoot:
            return 0
        depth = 0
        stack, tag = [], []
        pNode = pRoot
        while pNode or stack:
            while pNode:
                stack.append(pNode)
                tag.append(0)
                pNode = pNode.left
            if tag[-1] == 1:
                depth = max(depth, len(stack))
                stack.pop()
                tag.pop()
                pNode = None
            else:
                pNode = stack[-1]
                pNode = pNode.right
                tag.pop()
                tag.append(1)
        return depth