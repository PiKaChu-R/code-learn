#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   FindPath.py
    @Time    :   2019/09/09 11:47:09
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
    路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
    (注意: 在返回值的list中，数组长度大的数组靠前)
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def FindPath(root,target):
    if not root :
        return []
    if root.left == None and root.right == None:
        if sum == root.val:
            return [[root.val]]
        else:
            return []
    ans = []
    left = FindPath(root.left,target-root.val)
    right = FindPath(root.right,target-root.val)
    for i in left+right:
        ans.append([root.val]+i)
    ans = sorted(ans,key = len,reverse = True)
    return ans