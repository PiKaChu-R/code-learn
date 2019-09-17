#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   cutRope.py
    @Time    :   2019/09/17 20:17:00
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    给你一根长度为n的绳子,请把绳子剪成m段(m、n都是整数,n>1并且m>1),
    每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]
    可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度
    分别为2、3、3的三段，此时得到的最大乘积是18。
'''


# here put the import lib

class Solution:
    def cutRope(self, number):
        # write code here
        if number == 2:
            return 1
        if number == 3:
            return 2
        a,b = divmod(number,3)
        if b == 0:
            ans = 3**a
            number = b
        elif b == 1:
            ans = 3**(a-1)
            ans *= 4
        else:
            ans = 3**a
            ans *= 2
        return ans

s = Solution()
print(s.cutRope(8))