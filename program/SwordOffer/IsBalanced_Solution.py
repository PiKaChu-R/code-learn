#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   IsBalanced_Solution.py
    @Time    :   2019/09/09 16:34:52
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self,pRoot):
        if pRoot == None:
            return True
        if abs(self.getDepth(pRoot.left)-self.getDepth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    
    def getDepth(self,pRoot):
        if pRoot == None:
            return 0
        return max(self.getDepth(pRoot.left),self.getDepth(pRoot.right))+1