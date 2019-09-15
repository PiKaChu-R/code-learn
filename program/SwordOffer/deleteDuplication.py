#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   deleteDuplication.py
    @Time    :   2019/09/15 16:35:51
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    删除链表中重复的结点
    在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
    例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''


# here put the import lib
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # 使用了递归
        if not pHead:
            return pHead

        ans = node = pHead
        if node.next:
            if node.val != node.next.val:
                node.next = self.deleteDuplication(node.next)
            else:
                node = node.next
                while node.next:
                    if node.val != node.next.val:
                        return self.deleteDuplication(node.next)
                    node = node.next
                return node.next
        return ans
    
    def deleteDuplication2(self,pHead):
        # 不使用递归
        if not pHead:
            return pHead
        preHead = None
        pNode = pHead
        while pNode :
            needDelete = False
            nextNode = pNode.next
            if nextNode != None and nextNode.val == pNode.val:
                needDelete = True
            if needDelete == False:
                preHead = pNode
                pNode = pNode.next
            else:
                nodeVal = pNode.val
                pToBeDel = pNode
                while pToBeDel != None and pToBeDel.val == nodeVal:
                    pToBeDel = pToBeDel.next
                if preHead == None:
                    pHead = pToBeDel
                    pNode = pToBeDel
                    continue
                else:
                    preHead.next = pToBeDel
                pNode = preHead
        return pHead