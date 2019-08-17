#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 等差数列生成器
# 第一版
class ArithmeticProgression1:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None ->无穷数列

    def __iter__(self):
        # 先做加法，根据结果强制类型转换begin
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index
