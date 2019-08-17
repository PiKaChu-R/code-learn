Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import abc
>>> class Tombola(abc.ABC):
	@abc.abstractmethod
	def load(self,iterable):
		'''add item from iterable'''
	@abc.abstractclassmethod
	def pick(self):
		'''delete item randomly .If not self,return Error.'''
	def loaded(self):
		return bool(self.inspect())
	def inspect(self):
		items = []
		while True:
			try:
				items.append(self.pick())
			except LookupError:
				break
		self.load(items)
		return tuple(sorted(items))

	
>>> import random
>>> class BingoCage(Tombola):
	def __init__(self,items):
		self._randomizer = random.SystemRandom()
		self._items = []
		self.load(items)

		
>>> class BingoCage(Tombola):
	def __init__(self,items):
		self._randomizer = random.SystemRandom()
		self._items = []
		self.load(items)
	def load(self,items):
		self._items.extend(items)
		self._randomizer.shuffle(self._items)
	def pick(self):
		try:
			return self._items.pop()
		except IndexError:
			return LookupError('pick from empty BingoCage')
	def __call__(self):
		self.pick()

		
>>> class LotteryBlower(Tombola):
	def __init__(self,iterable):
		self._balls = list(iterable)
	def load(self,iterable):
		self._balls.extend(iterable)
	def pick(self):
		try:
			position = random.randrange(len(self._balls))
		except ValueError:
			raise LookupError('pick from empty LotteryBlower')
		return self._balls.pop(position)
	def loaded(self):
		return bool(self._balls)
	def inspect(self):
		return tuple(sorted(self._balls))

	
>>> @Tombola.register
    class TomboList(list):
	    
SyntaxError: unexpected indent
>>> @Tombola.register
class TomboList(list):
	def pick(self):
		if self:
			position = random.randrange(len(self))
			return self.pop(position)
		else:
			raise LookupError('pop from empty TomboList')
	load = list.extend
	def loaded(self):
		return bool(self)
	def inspect(self):
		return tuple(sorted(self))

	
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(BingoCage)
['__abstractmethods__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', 'inspect', 'load', 'loaded', 'pick']
>>> dir(TomboList)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'inspect', 'load', 'loaded', 'pick', 'pop', 'remove', 'reverse', 'sort']
>>> TomboList.__mro__
(<class '__main__.TomboList'>, <class 'list'>, <class 'object'>)
>>> class AddableBingoCage(bingoCage):
        def __add__(self,other):
                if isinstance(other,Tombola):
                        return AddableBingoCage(self.inspect()+other.inspect())
                else:
                        return NotImplemented
        def __iadd__(self,other):
                if isinstance(other,Tombola):
                        other_iterable = other.inspect()
                else:
                        try:
                                other_iterable = iter(other)
                        except TypeError:
                                self_cls = type(self).__name__
                                msg = 'right operand in += must be {!r} or an iterable'
                                raise TypeError(msg.format(self_cls))
                self.load(other_iterable)
                return self

