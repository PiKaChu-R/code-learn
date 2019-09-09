#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   ReverseList.py
    @Time    :   2019/09/09 10:44:18
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个链表，反转链表后，输出新链表的表头。
'''


# here put the import lib
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(pHead):
    if not pHead or not pHead.next:
        return pHead
    pre = None
    while pHead.next:
        node = pHead.next
        pHead.next = pre
        pre = pHead
        pHead = node
    pHead.next = pre
    return pHead