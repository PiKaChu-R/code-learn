#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   StackAndList.py
    @Time    :   2019/09/09 09:31:10
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    利用两个栈实现队列
    利用两个队列实现栈
'''


# here put the import lib
class Solution:
    # 栈实现队列
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if not self.stack1 and not self.stack2:
            return
        elif not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()


class Solution2:
    # 队列实现栈
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, val):
        if self.queue2 == []:
            self.queue1.append(val)
        else:
            self.queue2.append(val)

    def pop(self):
        if not self.queue1 and not self.queue2:
            return
        if self.queue1 != []:
            length = len(self.queue1)
            for i in range(length-1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        else:
            length = len(self.queue2)
            for i in range(length-1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()

P = Solution2()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())