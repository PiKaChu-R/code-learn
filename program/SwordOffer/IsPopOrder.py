#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   IsPopOrder.py
    @Time    :   2019/09/09 11:24:24
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    题目描述:输入两个整数序列，第一个序列表示栈的压入顺序，
    请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
    例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个
    弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
    （注意：这两个序列的长度是相等的）
'''


# here put the import lib
def IsPopOrder(pushV,popV):
    if not pushV or not popV :
        return False
    
    stack = []
    for i in pushV:
        stack.append(i)
        while len(stack) and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
    if stack:
        return False
    return True