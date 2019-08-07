#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   ranking.py
    @Time    :   2019/04/16 15:58:09
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   没明白题意
'''
''' 
    N个人参加比赛，进行排名，每个名次都可以并列，总共有多少种排列方法。
    例如：ABC个人参加比赛，比赛名次可以如下：1） A第一名、B第二名、C第三名 
          2）AB并列第一名，C第二名，等等。总共有13种排列方法。
    输入，例如
    2   //第一行为测试用例数目
    1   //参加的人数1
    3   //参加的人数3
    输出(结果对10000取模)
    1
    13
'''
# here put the import lib
import os
import sys
import math

def Rank(x):
    # print ("x:",x)
    if x == 0:
        return 0 
    if x == 1:
        return 1 

if __name__ == "__main__":
    k = int(input("The number of person:"))
    count = Rank(k)