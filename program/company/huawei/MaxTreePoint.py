#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   MaxTreePoint.py
    @Time    :   2019/09/08 19:55:38
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    二叉树的最大节点：分别实现前、中、后遍历，使用递归和非递归形式实现。
'''


# here put the import lib

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 构造完全二叉树

class Tree:
    lis = []

    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)

        if not self.root:
            self.root = node
            Tree.lis.append(self.root)
        else:
            while True:
                point = Tree.lis[0]

                if not point.left:
                    point.left = node
                    Tree.lis.append(point.left)
                    return
                elif not point.right:
                    point.right = node
                    Tree.lis.append(point.right)
                    Tree.lis.pop(0)
                    return


def PreTraver(root):
    # 递归版本
    if root == None:
        return []

    def helper(root):
        if not root:
            return
        res.append(root.val)
        helper(root.left)
        helper(root.right)

    res = []
    helper(root)
    return res


def PreTraver2(root):
    # 迭代版本
    if root == None:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def Postorder(root):
    # 递归版本
    if not root :
        return []
    res = []
    def helper(root):
        if not root:
            return
        helper(root.left)
        helper(root.right)
        res.append(root.val)
    helper(root)
    return res

def Postorder2(root):
    # 迭代版本
    if not root:
        return []
    res = []
    stack = [root,]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return res[::-1]

def inorderTraversal(root):
    # 递归版本
    if not root:
        return []
    res = []
    def helper(root):
        if not root:
            return 
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res

def inorderTraversal2(root):
    # 迭代版本
    if not root:
        return []
    
    res = []
    stack = []
    p = root
    while p or stack:
        while p:
            stack.append(p)
            p = p.left
        node = stack.pop()
        res.append(node.val)
        p = node.right
    return res