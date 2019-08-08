#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Function_peak.py
    @Time    :   2019/04/16 19:58:25
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''
''' 
    按数组的形式给出函数f(x)的取值，即数组A的A[0]元素为f(0)的取值，数组的取值都为整数，
函数在每个点都是严格单调递增或者严格递减（即A[i-1] != A[i] != A[i+1]），要求找出
最宽的先上升后下降的区间（这个区间内函数的值必须先上升到一个点然后下降，区间的上升
段和下降段长度必须都大于0）。
    1. 如果找到符合条件的最大区间输出数组对应的左右下标（保证只有一个最大区间）
    2. 找不到那么输出-1 -1
    输入格式
    n
    n长度的整数数组
    输出格式
    区间的范围
    输入样例
    10
    1 3 1 2 5 4 3 1 9 10
    输出样例
    2 7
    数据规模:对于 100% 的数据，1 <=n <=10, 000, 000
 '''
# here put the import lib
import sys

m = int(input())
list_num = []
k = input().strip().split()
# print(k)
if len(k)!=m:
        print ("数组长度与输入长度不符。")
        sys.exit()
for i in range(len(k)):
    n = int(k[i])
    # print (n+1)
    list_num.append(n)
# print (list_num,type(list_num))

l_list = [0]*m
r_list = [0]*m

#  left
for i in range(1, len(list_num)):
    # print(i)
    if list_num[i] > list_num[i-1]:
        # print (l_list[i-1])
        l_list[i] = l_list[i-1]+1

# right
for i in range(1, len(list_num)):
    k = len(list_num)-i-1
    if list_num[k] > list_num[k+1]:
        r_list[k] = r_list[k+1]+1

# print("l",l_list,"r",r_list)

mx = 0
ll = -1
rr = -1
for i in range(m):
    if(l_list[i] > 0 and r_list[i] > 0 and l_list[i]+r_list[i] > mx):
        mx = l_list[i]+r_list[i]
        ll = i-l_list[i]
        rr = i+r_list[i]

print (ll,rr)