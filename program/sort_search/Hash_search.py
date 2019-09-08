#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   Hash_search.py
    @Time    :   2019/06/24 15:12:45
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   哈希查找
'''

'''
算法流程：
    1.用给定的哈希函数构造哈希表；
    2.根据选择的冲突处理方法解决地址冲突；
    3.在哈希表的基础上执行哈希查找
复杂度：对于无冲突的hash表而言，查找复杂度为O(1)。
'''


# here put the import lib

class HashTable:
    def __init__(self,size):
        self.elem = [None for i in range(size)]
        self.count = size
    
    def hash(self,key):
        return key % self.count # 散列函数选择除留余数法

    def insert_hash(self,key):
        address = self.hash(key)
        while self.elem[address]:
            address = (address+1)%self.count
        self.elem[address] = key
    
    def search_hash(self,key):
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address+1)%self.count
            if not self.elem[address] or address == star:
                return False
        return True

if __name__ == "__main__":
    seq = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    hash_table = HashTable(len(seq))
    for i in seq:
        hash_table.insert_hash(i)

    for i in hash_table.elem:
        if i :
            print((i,hash_table.elem.index(i)),end=" ")
    
    print('\n')
    
    print(hash_table.search_hash(15))
    print(hash_table.search_hash(33))