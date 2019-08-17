Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> k = sum(x*x for x in range(1,8))
>>> k
140
>>> math.sqrt(k)
11.832159566199232
>>> k = sum(x*x for x in range(1,7))
>>> math.sqrt(k)
9.539392014169456
>>> help(sum)
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

>>> sum([1,2,3,4,5,6],4)
25
>>> hash(3)
3
>>> class Vector:
	typecode = 'd'
	def __init__(self,components):
		self._components = array(self.typecode,components)
	def __iter__(self):
		return iter(self._components)
	def __repr__(self):
		components = reprlib.repr(self._components)
		components = components[components.find('['):-1]
		return 'Vector({})'.format(components)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(self._components))
	def __eq__(self,other):
		if len(self) != len(other):
			return False
		for a,b in zip(self,other):
			if a!=b:
				return False
		return True
	def __abs__(self):
		return math.sqrt(sum(x*x for x in self))
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(memv)
	def __len__(self):
		return len(self._components)
	def __getitem__(self,index):
		cls = type(self)
		if isinstance(index,slice):
			return cls(self._components[index])
		elif isinstance(index,numbers.Integral):
			return self._components[index]
		else:
			msg = '{cls.__name__} indices must be integers'
			raise TypeError(msg.format(cls=cls))
	short_names = 'xyzt'
	def __getattr__(self,name):
		cls = type(self)
		if len(name)==1:
			pos = cls.short_names.find(name)
			if 0<=pos<len(self._components):
				return self._components[pos]
		msg = '{.__name__!r} object has no attribute {!r}'
		raise AttributeError(msg.format(cls,name))
	def __setattr__(self,name,value):
		cls = type(self)
		if len(name) == 1:
			if name in cls.short_names:
				error = 'readonly attribute {attr_name!r}'
			elif name.islower():
				error = "can't set attributes 'a' to 'z' in cls_name!r}"
			else:
				error = ""
			if error:
				msg = error.format(cls_name = cls.__name__,attr_name = name)
				raise AttributeError(msg)
		super().__setattr__(name,value)
	def __hash__(self):
		hashes = (hash(x) for x in self._components)
		return functools.reduce(operator.xor,hashes,0)
	def __angel__(self,n):
		r = math.sqrt(sum(x*x for x in self[n:]))
		a = math.atan2(r,self[n-1])
		if (n==len(self)-1)and(self[-1]<0):
			return math.pi*2-a
		else:
			return a
	def angles(self):
		return (self.angel(n) for n im range(1,len(self)))
	
SyntaxError: invalid syntax
>>> class Vector:
	typecode = 'd'
	def __init__(self,components):
		self._components = array(self.typecode,components)
	def __iter__(self):
		return iter(self._components)
	def __repr__(self):
		components = reprlib.repr(self._components)
		components = components[components.find('['):-1]
		return 'Vector({})'.format(components)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(self._components))
	def __eq__(self,other):
		if len(self) != len(other):
			return False
		for a,b in zip(self,other):
			if a!=b:
				return False
		return True
	def __abs__(self):
		return math.sqrt(sum(x*x for x in self))
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(memv)
	def __len__(self):
		return len(self._components)
	def __getitem__(self,index):
		cls = type(self)
		if isinstance(index,slice):
			return cls(self._components[index])
		elif isinstance(index,numbers.Integral):
			return self._components[index]
		else:
			msg = '{cls.__name__} indices must be integers'
			raise TypeError(msg.format(cls=cls))
	short_names = 'xyzt'
	def __getattr__(self,name):
		cls = type(self)
		if len(name)==1:
			pos = cls.short_names.find(name)
			if 0<=pos<len(self._components):
				return self._components[pos]
		msg = '{.__name__!r} object has no attribute {!r}'
		raise AttributeError(msg.format(cls,name))
	def __setattr__(self,name,value):
		cls = type(self)
		if len(name) == 1:
			if name in cls.short_names:
				error = 'readonly attribute {attr_name!r}'
			elif name.islower():
				error = "can't set attributes 'a' to 'z' in cls_name!r}"
			else:
				error = ""
			if error:
				msg = error.format(cls_name = cls.__name__,attr_name = name)
				raise AttributeError(msg)
		super().__setattr__(name,value)
	def __hash__(self):
		hashes = (hash(x) for x in self._components)
		return functools.reduce(operator.xor,hashes,0)
	def __angel__(self,n):
		r = math.sqrt(sum(x*x for x in self[n:]))
		a = math.atan2(r,self[n-1])
		if (n==len(self)-1)and(self[-1]<0):
			return math.pi*2-a
		else:
			return a
	def angles(self):
		return (self.angel(n) for n in range(1,len(self)))
	def __format__(self,fmt_spec=''):
		if fmt_spec.endswith('h'):
			fmt_spec = fmt_spec[:-1]
			coords = itertools.chain([abs(self)],self.angels())
			out_fmt = '<{}>'
		else:
			coords =self
			outer_fmt = '({})'
		components = (format(c,fmt-spec) for c in coords)
		return outer_fmt.format(', '.join(components))

	
>>> import math
>>> import itertools
>>> from array import array
>>> import functools
>>> import operator
>>> import numbers
>>> import reprlib
>>> 
