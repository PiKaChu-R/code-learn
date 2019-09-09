#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   PrintMinNumber.py
    @Time    :   2019/09/09 15:35:16
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的
    所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排
    成的最小数字为321323。
'''


# here put the import lib
def PrintMinNumber(nums):
    if not nums:
        return ''
    if len(nums) == 1:
        return nums[0]
    
    num = list(map(str,nums))
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if num[i]+num[j] > num[j]+nums[i]:
                nums[i],num[j] = num[j],num[i]
    return ''.join(num)