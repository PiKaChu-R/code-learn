#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Factorization.py
    @Time    :   2019/04/25 15:26:43
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    编写程序，用户从键盘输入小于1000的整数，对其进行因式分解。
    例如，10=2×5，60=2×2×3×5。
'''


# here put the import lib

x = input('Please input an integer less than 1000:')
x = eval(x)
t = x
i = 2
result = []
while True:
    if t==1:
        break
    if t%i==0:
        result.append(i)
        t = t/i
    else:
        i+=1
print(x,'=','*'.join(map(str,result)))