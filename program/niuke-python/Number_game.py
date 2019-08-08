#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   number_game.py
    @Time    :   2019/04/16 17:31:44
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''
'''
    给定任意一个整数，小C可以交换该数中任意的不同位，能够得到的最小数值是多少？前提是不能有前导0。
小C很快就给出了一个答案，小B希望你来帮她检验答案的正确性，你能帮忙吗？
'''
# here put the import lib
import math

old_num = input()
new_num = input()

list_old = sorted(list(old_num))
n = 0
if list_old[0] != '0':
    for i in range(len(list_old)):
        n = n+int(list_old[i])*(10**(len(list_old)-i-1))

else:
    for i in range(len(list_old)):
        if list_old[i]!="0":
            m = i
            break
    n = int(list_old[m])*(10**(len(list_old)-1))
    
    for i in range(m+1,len(list_old)):
        n = n+int(list_old[i])*(10**(len(list_old)-i-1))
if int(new_num) == n:
    print ("Yes")
else:
    # print (n)
    print ("No")