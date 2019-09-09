#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Fibonacci.py
    @Time    :   2019/09/09 09:52:39
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项
    （从0开始，第0项为0）。n<=39
    附加：跳台阶,变态跳台阶
'''


# here put the import lib
class Solution:
    def Fibonacci(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a

    def Jump(self, n):
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return n
        one_step_before = 2
        two_step_before = 1
        all_ways = 0
        for i in range(2, n):
            all_ways = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = all_ways
        return all_ways

    def JumpII(self,n):
        if n <= 0:
            return 0
        return pow(2,n-1)

s = Solution()
print(s.Jump(3))
