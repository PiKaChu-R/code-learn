#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Convert.py
    @Time    :   2019/09/09 14:21:35
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
    要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self,pRoot):
        if not pRoot:
            return pRoot
        if not pRoot.left and not pRoot.right:
            return pRoot
        
        self.Convert(pRoot.left)
        left = pRoot.left

        if left:
            while left.right:
                left = left.right
            pRoot.left ,left.right = left,pRoot
        
        self.Convert(pRoot.right)
        right = pRoot.right

        if right:
            while right.left:
                right = right.left
            pRoot.right,right.left = right,pRoot
        while pRoot.left:
            pRoot = pRoot.left
        
        return pRoot

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
newList = S.Convert(pNode1)
print(newList.val)