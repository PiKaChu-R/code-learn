#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Mirror.py
    @Time    :   2019/09/09 11:01:24
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    操作给定的二叉树，将其变换为源二叉树的镜像。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def Mirror(root):
    res = root

    def helper(r):
        if not r:
            return r
        if not r.left and r.right:
            return r
        tmp = TreeNode(-1)
        tmp.left = r.left
        tmp.right = r.right
        if tmp.right:
            r.left = helper(tmp.right)
        else:
            r.left = None
        if tmp.left:
            r.right = helper(tmp.left)
        else:
            r.right = None
        return r
    helper(root)
    return res


def Mirror2(root):
    if not root:
        return root
    root.left, root.right = root.right, root.left
    Mirror2(root.left)
    Mirror2(root.right)
    return root


def Mirror3(root):
    if root == None:
        return
    stackNode = []
    stackNode.append(root)
    while len(stackNode) > 0:
        nodeNum = len(stackNode) - 1
        tree = stackNode[nodeNum]
        stackNode.pop()
        nodeNum -= 1
        if tree.left != None or tree.right != None:
            tree.left, tree.right = tree.right, tree.left
        if tree.left:
            stackNode.append(tree.left)
            nodeNum += 1
        if tree.right:
            stackNode.append(tree.right)
            nodeNum += 1
