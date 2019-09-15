#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   isSymmetrical.py
    @Time    :   2019/09/15 16:59:13
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    请实现一个函数，用来判断一颗二叉树是不是对称的。
    注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        stack = []
        stack.append(pRoot.left)
        stack.append(pRoot.right)
        while stack:
            n2 = stack.pop()
            n1 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            stack.append(n1.left)
            stack.append(n2.right)
            stack.append(n1.right)
            stack.append(n2.left)
        return True
