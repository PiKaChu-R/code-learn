#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   mirror.py
    @Time    :   2019/08/19 16:29:56
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
 实现一个print反转输出类
'''


# here put the import lib
class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero !')
            return True


import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    # 错误异常处理添加
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero !'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)

def test():
    ''' This is a test program to vetify functoins of help.(Bingo) '''

if __name__ == "__main__":
    
    with looking_glass() as what:
        print('hello you and world')
        print(what)
