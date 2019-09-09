#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   reConstructBinaryTree.py
    @Time    :   2019/09/09 09:24:03
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的
    前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列
    {1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def reConstructBinaryTree(pre, tin):
    if not pre or not tin:
        return None
    
    BTree = TreeNode(pre[0])
    root = tin.index(pre[0])
    # if root != 0:
    BTree.left = reConstructBinaryTree(pre[1:root+1],tin[:root])
    # if root != len(tin)-1:
    BTree.right = reConstructBinaryTree(pre[root+1:],tin[root+1:])
    return BTree