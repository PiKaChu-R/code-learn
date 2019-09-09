#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   PrintFromTopToBottom.py
    @Time    :   2019/09/09 11:28:43
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def PrintFromTopToBottom(root):
    if not root:
        return []
    
    ans = []
    stack = [root]

    while stack:
        node = stack.pop(0)
        ans.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ans

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

# S = Solution()
print(PrintFromTopToBottom(pNode1))