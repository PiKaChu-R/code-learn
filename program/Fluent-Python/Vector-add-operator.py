Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
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
	def __neg__(self):
		return Vector(-x for x in self)
	def __pos__(self):
		return Vector(self)
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
	def __radd__(self.other):
		
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
	def __neg__(self):
		return Vector(-x for x in self)
	def __pos__(self):
		return Vector(self)
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
	def __add__(self,other):
		try:
			pairs = itertools.zip_longest(self,other,fillvalue=0.0)
			return Vector(a + b for a,b in pairs)
		except TypeError:
			return NotImplemented
	def __radd__(self,other):
		return self + other

	
>>> import math
>>> import itertools
>>> from array import array
>>> import functools
>>> import operator
>>> import numbers
>>> import reprlib
>>> v1 = Vector([1,2,3])
>>> v1 + 1
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    v1 + 1
TypeError: unsupported operand type(s) for +: 'Vector' and 'int'
>>> v1 + 'ABC'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    v1 + 'ABC'
TypeError: unsupported operand type(s) for +: 'Vector' and 'str'
>>> [1,2]@[2]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    [1,2]@[2]
TypeError: unsupported operand type(s) for @: 'list' and 'list'
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
	def __neg__(self):
		return Vector(-x for x in self)
	def __pos__(self):
		return Vector(self)
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
	def __add__(self,other):
		try:
			pairs = itertools.zip_longest(self,other,fillvalue=0.0)
			return Vector(a + b for a,b in pairs)
		except TypeError:
			return NotImplemented
	def __radd__(self,other):
		return self + other
	def __mul__(self,scalar):
		if isinstance(scalar,numbers.Real):
			return Vector(n * scalar for n in self)
		else:
			return NotImplemented
	def __rmul__(self,scalar):
		return self * scalar

	
>>> ayyar([1,2])@array([[2],[3]])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    ayyar([1,2])@array([[2],[3]])
NameError: name 'ayyar' is not defined
>>> array([1,2])@array([[2],[3]])
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    array([1,2])@array([[2],[3]])
TypeError: array() argument 1 must be a unicode character, not list
>>> array(b,[1,2])@array(b,[[2],[3]])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    array(b,[1,2])@array(b,[[2],[3]])
NameError: name 'b' is not defined
>>> help(array)
Help on class array in module array:

class array(builtins.object)
 |  array(typecode [, initializer]) -> array
 |  
 |  Return a new array whose items are restricted by typecode, and
 |  initialized from the optional initializer value, which must be a list,
 |  string or iterable over elements of the appropriate type.
 |  
 |  Arrays represent basic values and behave very much like lists, except
 |  the type of objects stored in them is constrained. The type is specified
 |  at object creation time by using a type code, which is a single character.
 |  The following type codes are defined:
 |  
 |      Type code   C Type             Minimum size in bytes 
 |      'b'         signed integer     1 
 |      'B'         unsigned integer   1 
 |      'u'         Unicode character  2 (see note) 
 |      'h'         signed integer     2 
 |      'H'         unsigned integer   2 
 |      'i'         signed integer     2 
 |      'I'         unsigned integer   2 
 |      'l'         signed integer     4 
 |      'L'         unsigned integer   4 
 |      'q'         signed integer     8 (see note) 
 |      'Q'         unsigned integer   8 (see note) 
 |      'f'         floating point     4 
 |      'd'         floating point     8 
 |  
 |  NOTE: The 'u' typecode corresponds to Python's unicode character. On 
 |  narrow builds this is 2-bytes on wide builds this is 4-bytes.
 |  
 |  NOTE: The 'q' and 'Q' type codes are only available if the platform 
 |  C compiler used to build Python supports 'long long', or, on Windows, 
 |  '__int64'.
 |  
 |  Methods:
 |  
 |  append() -- append a new item to the end of the array
 |  buffer_info() -- return information giving the current memory info
 |  byteswap() -- byteswap all the items of the array
 |  count() -- return number of occurrences of an object
 |  extend() -- extend array by appending multiple elements from an iterable
 |  fromfile() -- read items from a file object
 |  fromlist() -- append items from the list
 |  frombytes() -- append items from the string
 |  index() -- return index of first occurrence of an object
 |  insert() -- insert a new item into the array at a provided position
 |  pop() -- remove and return item (default last)
 |  remove() -- remove first occurrence of an object
 |  reverse() -- reverse the order of the items in the array
 |  tofile() -- write all items to a file object
 |  tolist() -- return the array converted to an ordinary list
 |  tobytes() -- return the array converted to a string
 |  
 |  Attributes:
 |  
 |  typecode -- the typecode character used to create the array
 |  itemsize -- the length in bytes of one array item
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __copy__(self, /)
 |      Return a copy of the array.
 |  
 |  __deepcopy__(self, unused, /)
 |      Return a copy of the array.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce_ex__(self, value, /)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Size of the array in memory, in bytes.
 |  
 |  append(self, v, /)
 |      Append new value v to the end of the array.
 |  
 |  buffer_info(self, /)
 |      Return a tuple (address, length) giving the current memory address and the length in items of the buffer used to hold array's contents.
 |      
 |      The length should be multiplied by the itemsize attribute to calculate
 |      the buffer length in bytes.
 |  
 |  byteswap(self, /)
 |      Byteswap all items of the array.
 |      
 |      If the items in the array are not 1, 2, 4, or 8 bytes in size, RuntimeError is
 |      raised.
 |  
 |  count(self, v, /)
 |      Return number of occurrences of v in the array.
 |  
 |  extend(self, bb, /)
 |      Append items to the end of the array.
 |  
 |  frombytes(self, buffer, /)
 |      Appends items from the string, interpreting it as an array of machine values, as if it had been read from a file using the fromfile() method).
 |  
 |  fromfile(self, f, n, /)
 |      Read n objects from the file object f and append them to the end of the array.
 |  
 |  fromlist(self, list, /)
 |      Append items to array from list.
 |  
 |  fromstring(self, buffer, /)
 |      Appends items from the string, interpreting it as an array of machine values, as if it had been read from a file using the fromfile() method).
 |      
 |      This method is deprecated. Use frombytes instead.
 |  
 |  fromunicode(self, ustr, /)
 |      Extends this array with data from the unicode string ustr.
 |      
 |      The array must be a unicode type array; otherwise a ValueError is raised.
 |      Use array.frombytes(ustr.encode(...)) to append Unicode data to an array of
 |      some other type.
 |  
 |  index(self, v, /)
 |      Return index of first occurrence of v in the array.
 |  
 |  insert(self, i, v, /)
 |      Insert a new item v into the array before position i.
 |  
 |  pop(self, i=-1, /)
 |      Return the i-th element and delete it from the array.
 |      
 |      i defaults to -1.
 |  
 |  remove(self, v, /)
 |      Remove the first occurrence of v in the array.
 |  
 |  reverse(self, /)
 |      Reverse the order of the items in the array.
 |  
 |  tobytes(self, /)
 |      Convert the array to an array of machine values and return the bytes representation.
 |  
 |  tofile(self, f, /)
 |      Write all items (as machine values) to the file object f.
 |  
 |  tolist(self, /)
 |      Convert array to an ordinary list with the same items.
 |  
 |  tostring(self, /)
 |      Convert the array to an array of machine values and return the bytes representation.
 |      
 |      This method is deprecated. Use tobytes instead.
 |  
 |  tounicode(self, /)
 |      Extends this array with data from the unicode string ustr.
 |      
 |      Convert the array to a unicode string.  The array must be a unicode type array;
 |      otherwise a ValueError is raised.  Use array.tobytes().decode() to obtain a
 |      unicode string from an array of some other type.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  itemsize
 |      the size, in bytes, of one array item
 |  
 |  typecode
 |      the typecode character used to create the array
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> array('b',[1,2])@array('b',[[2],[3]])
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    array('b',[1,2])@array('b',[[2],[3]])
TypeError: an integer is required (got type list)
>>> array('b',[1,2])@array('b',[2,3])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    array('b',[1,2])@array('b',[2,3])
TypeError: unsupported operand type(s) for @: 'array.array' and 'array.array'
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
		if isinstance(other,Vector):
			return (len(self) == len(other) and all(a == b for a,b in zip(self,other)))
		else:
			return NotImplemented
	def __abs__(self):
		return math.sqrt(sum(x*x for x in self))
	def __neg__(self):
		return Vector(-x for x in self)
	def __pos__(self):
		return Vector(self)
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
	def __add__(self,other):
		try:
			pairs = itertools.zip_longest(self,other,fillvalue=0.0)
			return Vector(a + b for a,b in pairs)
		except TypeError:
			return NotImplemented
	def __radd__(self,other):
		return self + other
	def __mul__(self,scalar):
		if isinstance(scalar,numbers.Real):
			return Vector(n * scalar for n in self)
		else:
			return NotImplemented
	def __rmul__(self,scalar):
		return self * scalar

	
>>> 
