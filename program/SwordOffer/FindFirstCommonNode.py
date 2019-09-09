#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   FindFirstCommonNode.py
    @Time    :   2019/09/09 16:06:02
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入两个链表，找出它们的第一个公共结点。
'''


# here put the import lib
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self,pHead1,pHead2):
        count1 = 0
        count2 = 0
        p1 = pHead1
        p2 = pHead2
        common = None
    
        while p1:
            count1 +=1
            p1 = p1.next
        while p2:
            count2 += 1
            p2 = p2.next
        
        if (count1 - count2) >0:
            sub = count1 - count2
            while sub:
                pHead1 = pHead1.next
                sub -= 1
        else:
            sub = count2 - count1
            while sub:
                pHead2 = pHead2.next
                sub -= 1
        
        n1 = pHead1
        n2 = pHead2
        while n1 and n2:
            if n1.val == n2.val:
                common = n1
                return common
            else:
                n1 = n1.next
                n2 = n2.next
        return common