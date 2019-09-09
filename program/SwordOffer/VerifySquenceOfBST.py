#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   VerifySquenceOfBST.py
    @Time    :   2019/09/09 11:40:30
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
    如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''


# here put the import lib
def VerifySquenceOfBST(seq):
    if not seq:
        return False
    n = len(seq)
    if n == 1:
        return True
    
    last = n-1
    while last > 0 :
        i = 0
        while seq[i] < seq[last]:
            i += 1
        while seq[i] > seq[last]:
            i += 1
        if i < last:
            return False
        last -= 1
    return True