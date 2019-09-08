#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Test1.py
    @Time    :   2019/09/07 19:22:49
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    华为笔试第一题：给定三角形周长p，求满足边长为整数且周长为p的直角三角形个数。
'''


# here put the import lib

if __name__ == "__main__":
    c = int(input())
    ans = 0
    # n的意义是，最小直角边不可能超过边长的1/3
    n = c // 3  
    for i in range(1, n):
        # 通过 i+j+k=c以及i^2+j^2=k^2推导而来
        j = c-c*c/(2*c-2*i)  
        # 1e-5的原因：将误差缩小到0.00001
        if i < j and j-(int(j)) < 1e-5:
            ans += 1
    print(ans)
