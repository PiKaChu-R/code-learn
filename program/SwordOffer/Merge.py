#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Merge.py
    @Time    :   2019/09/09 10:51:40
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入两个单调递增的链表，
    输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


# here put the import lib
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def Merge(pHead1,pHead2):
    if pHead1 == None:
        return pHead2
    if pHead2 == None:
        return pHead1
    res = new = ListNode(0)
    while pHead1 and pHead2:
        if pHead1.val < pHead2.val:
            new.next = pHead1
            pHead1 = pHead1.next
        else:
            new.next = pHead2
            pHead2 = pHead2.next
        new = new.next
    
    if pHead1:
        new.next = pHead1
    if pHead2 :
        new.next = pHead2
    return res.next