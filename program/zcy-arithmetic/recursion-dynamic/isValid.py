#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   isValid.py
    @Time    :   2019/09/03 20:58:27
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    表达式得到期望结果的组成种数
    
    给定一个只由0(假)，1（真），&（逻辑与），|（逻辑或），^（异或）五种字符组成的字符串，记为exp；还有一个布尔型的值，记为desired。
    写一个函数，返回exp能有多少种小括号的组合方式，可以达到desired的结果。
    例如： expression：1^0|0|1 desired：false
    只有两种组合可以得到false： 1^((0|0)|1)和1^(0|(0|1)) 所以应该返回2。
'''


# here put the import lib

# 动态规划的方法生成两个大小为NxN的矩阵t和f，t表示[j...i]为True的种数，f表示为False的种数。时间O(n^3)，空间O(n^2)。

def isVaild(s):
    if len(s) & 1 == 0:
        return False
    
    for i in range(0,len(s),2):
        if s[i]!='1' and s[i]!='0':
            return False

    for i in range(1,len(s),2):
        if s[i]!='&' and s[i]!='|' and s[i] != '^':
            return False
    return True

def num2(express,desired):
    if express == None or express == '':
        return 0
    
    if not isVaild(express):
        return 0
    
    t = [[0]*len(express) for _ in range(len(express))]
    f = [[0]*len(express) for _ in range(len(express))]
    if express[0] == '0':
        t[0][0] = 0
        f[0][0] = 1
    else:
        t[0][0] = 1
        f[0][0] = 0
    
    for i in range(2,len(express),2):
        if express[i] == '0':
            t[i][i] = 0
            f[i][i] = 1
        else:
            t[i][i] = 1
            f[i][i] = 0
        for j in range(i-2,-1,-2):
            for k in range(j,i,2):
                if express[k+1] =='&':
                    t[j][i] += t[j][k]*t[k+2][i]
                    f[j][i] += (f[j][k]+t[j][k])*f[k+2][i]+f[j][k]*t[k+2][i]
                elif express[k+1] == '|':
                    t[j][i] += (f[j][k]+t[j][k])*t[k+2][i]+t[j][k]*f[k+2][i]
                    f[j][i] += f[j][k]*f[k+2][i]
                else:
                    t[j][i] += f[j][k] * t[k+2][i] + t[j][k] * f[k+2][i]
                    f[j][i] += f[j][k] * f[k+2][i] + t[j][k] * t[k+2][i]
    
    if desired:
        return t[0][-1]
    else:
        return f[0][-1]

express = '1^0|0|1'
desired = False
# print(num2(express,desired))
