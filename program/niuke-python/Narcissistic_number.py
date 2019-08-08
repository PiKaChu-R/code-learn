#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Narcissistic_number.py
    @Time    :   2019/04/17 16:04:19
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    水仙花数，输入一个数值范围，其中有水仙花数就从小到大输出，否则输出no
    样例输入
    100 120
    300 380
    样例输出
    no
    370 371
'''


# here put the import lib

def Narcissistic_1(list_num):

    Nar_list = [153,370,371,407]

    out_list = []

    for i in range(0,4):
        if Nar_list[i] >= list_num[0] and Nar_list[i] <= list_num[1]:
            out_list.append(Nar_list[i])

    if len(out_list) == 0:
        print ('No.')
    else:
        k = ''
        for i in range(len(out_list)):
            m = str(out_list[i])
            k = k + m +' '
            # print (out_list[i])
        print (k)


def Narcissistic_2(list_num):

    # print('2')
    
    out_list = []

    for i in range(list_num[0],list_num[1]+1):
        m = (i%100)%10
        n = (i%100-m)/10
        k = (i-n*10-m)/100
        if (k**3+n**3+m**3) == i:
            out_list.append(i)
    
    if len(out_list) == 0:
        print ('No.')
    else:
        k = ''
        for i in range(len(out_list)):
            m = str(out_list[i])
            k = k + m +' '
            # print (out_list[i])
        print (k)


if __name__ == "__main__":
    
    num = input("Input the number(100-999):").strip().split()
    
    num_list = []
    for i in range(len(num)):
        num_list.append(int(num[i]))

    Narcissistic_1(num_list)
    Narcissistic_2(num_list)
