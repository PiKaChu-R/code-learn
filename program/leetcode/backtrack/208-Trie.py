#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   208-Trie.py
    @Time    :   2019/08/08 19:53:29
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   实现前缀树
'''

'''
    实现前缀树
'''


# here put the import lib

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = dict()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        
        tmp = self._dict
        for i in word:
            if i not in tmp:
                tmp[i] = {}
            tmp = tmp[i]
        tmp['end'] = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        tmp = self._dict
        for i in word:
            if i not in tmp:
                return False
            tmp = tmp[i]
        return 'end' in tmp
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self._dict
        for c in prefix:
            if not c in tmp:
                return False
            tmp = tmp[c]
        return  True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)


# so = Solution()
# k = so.readBinaryWatch(4)
# print(k)



