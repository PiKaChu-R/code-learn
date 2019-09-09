#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   printListFromTailToHead.py
    @Time    :   2019/09/09 09:19:43
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''


# here put the import lib
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def printListFromTailToHead(listNode):
    if not listNode:
        return []
    arraylist = []
    while listNode:
        arraylist.insert(0,listNode.val)
        listNode = listNode.next
    return arraylist