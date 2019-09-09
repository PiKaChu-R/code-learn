#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   NumberOf1Between1AndN_Solution.py
    @Time    :   2019/09/09 15:31:17
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
    1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''


# here put the import lib
def NumberOf1Between1AndN_Solution(n):
    count = 0
    m = 1 
    while m <= n:
        count += (n//m+8)//10*m + (n//m%10 == 1) * (n%m+1)
        m *= 10
    return count

def NumberOf1Between1AndN2(n):
    ones, m = 0, 1
    while m <= n:
        if ((n // m) % 10) != 0 and ((n // m) % 10) != 1:
            ones += (n // 10 // m + 1) * m
        elif ((n // m) % 10) == 1:
            ones += (n // m // 10) * m + n % m + 1
        m *= 10
    return ones