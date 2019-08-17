#!/usr/bin/env python
# -*- coding: utf-8 -*-


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


# 使用itertools中的count和takewhile函数
import itertools

# aritprog_gen_v3 不再是生成器函数，因为在定义体中没有yield关键字，但是会返回一个
# 生成器，因此与其它生成器函数一样，也是生成器工厂函数。
def aritprog_gen_v3(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen
