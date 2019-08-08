#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @File    :   211-AddandSearch-DataStructDesign.py
    @Time    :   2019/08/08 20:21:41
    @Author  :   R.
    @Version :   1.0
    @Contact :   827710637@qq.com
    @Desc    :   None
'''

'''
    设计一个支持以下两种操作的数据结构：
        void addWord(word)
        bool search(word)
    search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 
    或 a-z 。 . 可以表示任何一个字母。
'''


# here put the import lib

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self._dict = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """

        tmp = self._dict
        for c in word:
            if c not in tmp:
                tmp[c] = {}
            tmp = tmp[c]
        tmp['end'] = True
        # print(self._dict)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cut = False

        def helper(d,s):
            nonlocal cut 
            if cut :
                return True  
            tmp = d
            for i ,c in enumerate(s):
                if c =='.':
                    return sum(helper(tmp[j],s[i+1:]) for j in tmp if j != 'end')
                if c not in tmp:
                    return False
                tmp = tmp[c]
            cut = 'end' in tmp
            return cut

        return helper(self._dict,word)



# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('map')
obj.addWord('dad')
param_2 = obj.search('d.a')
print (param_2)


# so = Solution()
# k = so.readBinaryWatch(4)
# print(k)
