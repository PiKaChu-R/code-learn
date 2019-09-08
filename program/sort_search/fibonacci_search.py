#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   fibonacci_search.py
    @Time    :   2019/06/24 14:57:07
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   斐波那契查找
'''

'''
斐波那契被递归方法如下定义：F(1)=1，F(2)=1，F(n)=f(n-1)+F(n-2) （n>=2）
算法描述：
    在二分查找的基础上根据斐波那契数列进行分割的.
'''


# here put the import lib

def fibonacci_search(seq, key):
    F = [1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
     233, 377, 610, 987, 1597, 2584, 4181, 6765,
     10946, 17711, 28657, 46368]
    
    low = 0
    high = len(seq) -1 
    k = 0
    while high > F[k] -1:
        k += 1
    print(k)
    i = high
    while F[k]-1>i:
        seq.append(seq[high])
        i+=1
    print (seq)

    time = 0
    while low <= high:
        time += 1
        if k<2:
            mid = low
        else:
            mid = low+F[k-1]-1
        
        print("low=%s, mid=%s, high=%s" % (low, mid, high))
        if key <seq[mid]:
            high = mid -1 
            k -= 1
        elif key>seq[mid]:
            low = mid +1
            k -=2
        else:
            if mid <= high :
                print('time:%s'%time)
                return high
            else:
                print('time:%s'%time)
                return high
    print('time:%s'%time)
    return False

if __name__ == "__main__":
    seq = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = fibonacci_search(seq, 444)
    print(result)
