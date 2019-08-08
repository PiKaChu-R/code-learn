Trie：
		LeetCode：208、211
1.前缀树，典型应用对象是字符串，可以用于保存，统计。
2.特点是：**用边表示字符**。
3.优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希表高。
4.常用方法是构建类：
``` python?linenums
class Node:
	def __init__(self):
		self.is_word = False
		self.next = [None for _ in range(26)]
```
5.Python 中可以使用字典来实现：

``` python?linenums
class Trie:

	def __init__(self):
		self._dict = {}
		
	def add(self,word):
		tmp = self._dict
		for c in word:
			if c not in tmp:
				tmp[c] = {}
			tmp = tmp[c]
```

