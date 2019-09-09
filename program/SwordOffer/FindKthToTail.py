#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   FindKthToTail.py
    @Time    :   2019/09/09 10:36:33
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个链表，输出该链表中倒数第k个结点。
'''


# here put the import lib
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def FindKthToTail(head,k):
    if not head:
        return 
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    while fast:
        fast = fast.next
        k -= 1
    slow = dummy
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    return slow.next.val
    # 返回删除后的链表头结点
    # slow.next= slow.next.next
    # return dummy.enxt