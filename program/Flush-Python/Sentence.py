Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> import reprlib
>>> RE_WORD = re.compile('\w+')
>>> class Swntence:
	def __init__(self,text):
		self.text = text
		self.words = RE_WORD.findall(text)
	def __getitem__(self,index):
		return self.words[index]
	def __len__(self):
		return len(self.words)
	def __repr__(self):
		return 'Sentence(%s)'%reprlib.repr(self.text)

	
>>> so = Swntence('hello word and you')
>>> so
Sentence('hello word and you')
>>> so.text
'hello word and you'
>>> so.words
['hello', 'word', 'and', 'you']
>>> so = Swntence('"The time has come," the Walrus said,')
>>> so
Sentence('"The time ha... Walrus said,')
>>> list(so)
['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
>>> 
