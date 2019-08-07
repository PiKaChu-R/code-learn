Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import collections
>>> Card = collections.namedtuple("Card",['rank','suit'])
>>> class FrenckDeck2(collections.MutableSequence):
	ranks = [str(n) for n in range(2,11)]+list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	
>>> class FrenckDeck2(collections.MutableSequence):
	ranks = [str(n) for n in range(2,11)]+list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()
	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
	def __len__(self):
		return len(self._cards)
	def __getitem__(self,position):
		return self._cards[position]
	def _-setitem__(self,position,value):
		
SyntaxError: invalid syntax
>>> class FrenckDeck2(collections.MutableSequence):
	ranks = [str(n) for n in range(2,11)]+list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()
	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
	def __len__(self):
		return len(self._cards)
	def __getitem__(self,position):
		return self._cards[position]
	def __setitem__(self,position,value):
		self._cards[position] =value
	def __delitem__(self,position):
		del self._cards[position]
	def insert(self,position,value):
		self._cards.insert(position,value)

		
>>> class FrenchDeck:
	ranks = [str(n) for n in range(2,11)] +list('JQK')
	suits = 'spades diamonds clubs hearts'.split()
	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
	def __len__(self):
		return len(self._cards)
	def __getitem__(self,position):
		return self._cards[position]

	
>>> class FrenchDeck(collections.MutableSequence):
	ranks = [str(n) for n in range(2,11)] +list('JQK')
	suits = 'spades diamonds clubs hearts'.split()
	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
	def __len__(self):
		return len(self._cards)
	def __getitem__(self,position):
		return self._cards[position]

	
>>> F= FrenchDeck()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    F= FrenchDeck()
TypeError: Can't instantiate abstract class FrenchDeck with abstract methods __delitem__, __setitem__, insert
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(list.__contains__)
Help on wrapper_descriptor:

__contains__(self, key, /)
    Return key in self.

>>> 
