#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   demo_executor_map.py
    @Time    :   2019/08/23 10:34:26
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    验证executor.map()
'''


# here put the import lib
from time import sleep, strftime
from concurrent import futures

def display(*args): 
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)
def loiter(n): 
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    if n == 0:
        sleep(10)
    else:
        sleep(1)
    # sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10 
def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3) 
    results = executor.map(loiter, range(5)) 
    display('results:', results) 
    display('Waiting for individual results:')
    for i, result in enumerate(results): 
        display('result {}: {}'.format(i, result))
main()