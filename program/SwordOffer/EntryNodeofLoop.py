#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   EntryNodeofLoop.py
    @Time    :   2019/09/15 16:14:35
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    一个链表中包含环，请找出该链表的环的入口结点。
'''


# here put the import lib
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeofLoop(self,pHead):
        d = dict()
        r = pHead
        while r :
            if r.val in d.keys():
                return r
            else:
                d[r.val] = 1
            r = r.next
        return None
    
    def EntryNodeofLoop2(self,pHead):
        if not pHead or not pHead.next:
            return None
        fast = pHead
        slow = pHead
        while fast and fast.next:
            if fast == slow:
                break
            fast = fast.next.next
            slow = slow.next
        
        if slow != fast:
            return None

        slow = pHead
        while fast:
            if fast == slow:
                return fast
            slow = slow.next
            fast = fast.next