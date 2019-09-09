#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Sum_Solution.py
    @Time    :   2019/09/09 17:29:33
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    求1+2+3+...+n，要求不能使用乘除法、
    for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''


# here put the import lib
def Sum_Solution(n):
    import math
    return int(math.pow(n,2)+n)>>1