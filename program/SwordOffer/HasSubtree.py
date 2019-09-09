#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   HasSubtree.py
    @Time    :   2019/09/09 10:56:07
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入两棵二叉树A，B，判断B是不是A的子结构。
    （ps：我们约定空树不是任意一个树的子结构）
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def HasSubtree(pRoot1,pRoot2):
    if not pRoot1 or not pRoot2:
        return False
    
    def helper(root1,root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val == root2.val:
            return helper(root1.left,root2.left) and helper(root1.right,root2.right)
        else:
            return False

    flag = False
    if pRoot1.val == pRoot2.val:
        flag = helper(pRoot1,pRoot2)
    if not flag:
        flag = (HasSubtree(pRoot1.left,pRoot2)) or (HasSubtree(pRoot1.right,pRoot2))
    return flag