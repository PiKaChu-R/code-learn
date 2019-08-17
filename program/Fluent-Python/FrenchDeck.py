Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import collections
>>> Card = collections.namedtuple('Card',['rank','suit'])
>>> class FrenchDeck:
	ranks = [str(n) for n in range(2,11)] +list('JQK')
	suits = 'spades diamonds clubs hearts'.split()

	
>>> class FrenchDeck:
	ranks = [str(n) for n in range(2,11)] +list('JQK')
	suits = 'spades diamonds clubs hearts'.split()
	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

		
>>> class FrenchDeck:
	ranks = [str(n) for n in range(2,11)] +list('JQK')
	suits = 'spades diamonds clubs hearts'.split()
	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
	def __len__(self):
		return len(self._cards)
	def __getitem__(self,position):
		return self._cards[position]

	
>>> 
