#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   GetNext.py
    @Time    :   2019/09/15 16:50:14
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
    注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''


# here put the import lib
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return pNode
        
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return pNode.next
            pNode = tmp
        
        return None