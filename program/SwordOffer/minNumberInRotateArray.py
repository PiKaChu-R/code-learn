#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   minNumberInRotateArray.py
    @Time    :   2019/09/09 09:45:00
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
    例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
    NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


# here put the import lib
class Solution:
    def minNumberInRotateArray(self,rotateArray):
        if not rotateArray:
            return 0
        
        left = 0
        right = len(rotateArray)-1
        low = min(rotateArray[0],rotateArray[-1])
        while left <= right:
            mid = left + (right-left)//2
            if rotateArray[mid] < low:
                low = rotateArray[mid]
                right = mid -1
            else:
                left = mid + 1
        return low
