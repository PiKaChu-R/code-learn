#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   SerializeAndDese.py
    @Time    :   2019/09/15 17:21:12
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        # 采用前序方式
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self,s):
        # 解析前序
        Nodes = s.split(',')
        def helper(node):
            if len(node) <= 0:
                return None
            val = node.pop(0)
            root = None
            if val != '#':
                root = TreeNode(int(val))
                root.left = helper(node)
                root.right = helper(node)
            return root
        return helper(Nodes)