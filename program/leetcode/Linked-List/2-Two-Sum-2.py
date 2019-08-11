#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   2-sum-2.py
    @Time    :   2019/06/05 11:33:07
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 
逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# here put the import lib

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def addTwonumbers(self,l1,l2):

        n = l1.val + l2.val
        l3 = ListNode(n%10)
        l3.next = ListNode(n//10)
        p1 = l1.next
        p2 = l2.next
        p3 = l3
        while True:
            if p1 and p2:
                sum = p1.val + p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p2 = p2.next
                p3 = p3.next
            elif p1 and not p2:
                sum = p1.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p3 = p3.next
            elif not p1 and p2:
                sum = p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p2 = p2.next
                p3 = p3.next
            else:
                if p3.next.val == 0:
                    p3.next = None
                break
        return l3


if __name__ == "__main__":
    k1 = list(map(int,input().split()))
    k2 = list(map(int,input().split()))
    l1 = ListNode(0)
    l2 = ListNode(0)
    temp1 = l1
    temp2 = l2
    for i in range(len(k1)):
        l1.next = ListNode(k1[i])
        l1 = l1.next
    for i in range(len(k2)):
        l2.next = ListNode(k2[i])
        l2 = l2.next

    l1 = temp1.next
    l2 = temp2.next

    solution = Solution()
    l3 = solution.addTwonumbers(l1,l2)

    print(l3.next.next.val)