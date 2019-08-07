#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Geohash_code.py
    @Time    :   2019/04/22 17:42:27
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    geohash 常用于将二维的经纬度转换为字符串，分为两步：第一步是经纬度的二进制编码，
    第二部是 base32 转码。此题考察唯独的二进制编码：算法对维度 [-90,90] 通过二分法
    进行无限逼近（取决于所需精度，本题精度为 6 ）。注意，本题进行二分法逼近过程中只
    采用向下取整来进行二分，针对二分中间值属于右区间。算法举例如下：
    （1） 区间 [-90,90] 进行二分为 [-90,0),[0,90] ，成为左右区间，可以确定 80 为右区间，标记为 1 ；
    （2） 针对上一步的右区间 [0,90] 进行二分为 [0,45),[45,90] ，可以确定 80 是右区间，标记为 1 ；
    （3） 针对 [45,90] 进行二分为 [45,67),[67,90] ，可以确定 80 为右区间，标记为 1 ；
    （4） 针对 [67,90] 进行二分为 [67,78),[78,90] ，可以确定 80 位右区间，标记为 1 ；
    （5） 针对 [78,90] 进行二分为 [89,84),[84,90] ，可以确定 80 位左区间，标记为 0 ；
    （6） 针对 [78,84) 进行二分为 [78,81),[81,84) ，可以确定 80 位左区间，标记为 0 ；
    已达精度要求，编码为 111100
    样本输入： 80
    样本输出： 111100
'''


# here put the import lib
import math

if __name__ == "__main__":

    left = -90
    right = 90
    mid = 0
    flag = 6
    output = ''
    flag_l = '0'
    flag_r = '1'

    key_num = int(input())

    while flag != 0:
        flag -= 1
        if key_num <= mid and key_num >= left:
            output += flag_l
            right = mid
            mid = math.floor((left + right)/2)

        elif key_num >= mid and key_num <= right:
            output += flag_r
            left = mid
            mid = math.floor((left + right)/2)

    print (output)