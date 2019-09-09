#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   MinStack.py
    @Time    :   2019/09/09 11:14:37
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    定义栈的数据结构，
    请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''


# here put the import lib
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val < self.min():
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min())

    def pop(self):
        if self.min_stack == [] or self.stack == []:
            return None
        self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
