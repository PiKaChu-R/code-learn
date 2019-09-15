#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Print.py
    @Time    :   2019/09/15 17:10:54
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    请实现一个函数按照之字形打印二叉树，
    即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''


# here put the import lib
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []

        ans = []
        tmp = [pRoot]
        flag = False

        while tmp:
            new = []
            res = []
            for i in tmp:
                if i:
                    res.append(i.val)
                    new.append(i.left)
                    new.append(i.right)
            if not res:
                break
            if flag:
                res = res[::-1]
                flag = False
            else:
                flag = True
            ans.append(res)
            tmp = new
        return ans
