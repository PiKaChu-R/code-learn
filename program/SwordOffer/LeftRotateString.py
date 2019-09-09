#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   LeftRotateString.py
    @Time    :   2019/09/09 16:59:08
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，
    就是用字符串模拟这个指令的运算结果。
    对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
    例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
'''


# here put the import lib
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return s
        k = n % len(s)
        return s[k:]+s[:k]

    def LeftRotateString2(self, s, n):
        if len(s) <= 0 or len(s) < n or n < 0:
            return ''
        strList = list(s)
        self.Reverse(strList)
        length = len(s)
        pivot = length - n
        frontList = self.Reverse(strList[:pivot])
        behindList = self.Reverse(strList[pivot:])
        resultStr = ''.join(frontList) + ''.join(behindList)
        return resultStr

    def Reverse(self, alist):
        if alist == None or len(alist) <= 0:
            return ''
        startIndex = 0
        endIndex = len(alist) - 1
        while startIndex < endIndex:
            alist[startIndex], alist[endIndex] = alist[endIndex], alist[startIndex]
            startIndex += 1
            endIndex -= 1
        return alist
