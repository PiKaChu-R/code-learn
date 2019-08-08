Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Vectord2d:
        __slots__ = ('__x','__y')
	typecode = 'd'
	def __init__(self,x,y):
		self.__x = float(x)
		self.__y = float(y)
	def __iter__(self):
		return (i for i in (self.x,self.y))
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r},{!r})'.format(class_name,*self)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))
	def __eq__(self,other):
		return tuple(self) == tuple(other)
	def __abs__(self):
		return math.hypot(self.x,self.y)
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(*memv)
	def angle(self):
		return math.atan2(self.x,self.y)
	def __format__(self,fmt_spec = ''):
		if fmt_spec.endswith('p'):
			fmt_spec = fmt_spec[:-1]
			coords = (abs(self),self.angle())
			outer_fmt = '<{},{}>'
		else:
			coords = self
			outer_fmt = '({},{})'
		components = (format(c,fmt_spec) for c in coords)
		return outer_fmt.format(*components)
	@property
	def x(self):
		return self.__x
	@property
	def y(self):
		return self.__y
	def __iter__(self):
		return (i for i in (self.x,self.y))
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class Vectord2d:
        __slots__ = ('__x','__y')
        
	typecode = 'd'
	
	def __init__(self,x,y):
		self.__x = float(x)
		self.__y = float(y)
	def __iter__(self):
		return (i for i in (self.x,self.y))
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r},{!r})'.format(class_name,*self)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))
	def __eq__(self,other):
		return tuple(self) == tuple(other)
	def __abs__(self):
		return math.hypot(self.x,self.y)
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(*memv)
	def angle(self):
		return math.atan2(self.x,self.y)
	def __format__(self,fmt_spec = ''):
		if fmt_spec.endswith('p'):
			fmt_spec = fmt_spec[:-1]
			coords = (abs(self),self.angle())
			outer_fmt = '<{},{}>'
		else:
			coords = self
			outer_fmt = '({},{})'
		components = (format(c,fmt_spec) for c in coords)
		return outer_fmt.format(*components)
	@property
	def x(self):
		return self.__x
	@property
	def y(self):
		return self.__y
	def __iter__(self):
		return (i for i in (self.x,self.y))
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> class Vectord2d:
	__slots__ = ('__x','__y')

	typecode = 'd'

	def __init__(self,x,y):
		self.__x = float(x)
		self.__y = float(y)
	def __iter__(self):
		return (i for i in (self.x,self.y))
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r},{!r})'.format(class_name,*self)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))
	def __eq__(self,other):
		return tuple(self) == tuple(other)
	def __abs__(self):
		return math.hypot(self.x,self.y)
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(*memv)
	def angle(self):
		return math.atan2(self.x,self.y)
	def __format__(self,fmt_spec = ''):
		if fmt_spec.endswith('p'):
			fmt_spec = fmt_spec[:-1]
			coords = (abs(self),self.angle())
			outer_fmt = '<{},{}>'
		else:
			coords = self
			outer_fmt = '({},{})'
		components = (format(c,fmt_spec) for c in coords)
		return outer_fmt.format(*components)
	@property
	def x(self):
		return self.__x
	@property
	def y(self):
		return self.__y
	def __iter__(self):
		return (i for i in (self.x,self.y))

	
>>> dir(Vectord2d)
['_Vectord2d__x', '_Vectord2d__y', '__abs__', '__bool__', '__bytes__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', 'angle', 'frombytes', 'typecode', 'x', 'y']
>>> class Vectord2d:
	typecode = 'd'

	def __init__(self,x,y):
		self.__x = float(x)
		self.__y = float(y)
	def __iter__(self):
		return (i for i in (self.x,self.y))
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r},{!r})'.format(class_name,*self)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))
	def __eq__(self,other):
		return tuple(self) == tuple(other)
	def __abs__(self):
		return math.hypot(self.x,self.y)
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(*memv)
	def angle(self):
		return math.atan2(self.x,self.y)
	def __format__(self,fmt_spec = ''):
		if fmt_spec.endswith('p'):
			fmt_spec = fmt_spec[:-1]
			coords = (abs(self),self.angle())
			outer_fmt = '<{},{}>'
		else:
			coords = self
			outer_fmt = '({},{})'
		components = (format(c,fmt_spec) for c in coords)
		return outer_fmt.format(*components)
	@property
	def x(self):
		return self.__x
	@property
	def y(self):
		return self.__y
	def __iter__(self):
		return (i for i in (self.x,self.y))

	
>>> class ShortVec2d(Vectord2d):
	typecode = 'f'

	
>>> sv = ShortVec2d(1/11,1/27)
>>> sv
ShortVec2d(0.09090909090909091,0.037037037037037035)
>>> len(bytes(sv))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    len(bytes(sv))
  File "<pyshell#7>", line 15, in __bytes__
    return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))
NameError: name 'array' is not defined
>>> from array import array
>>> len(bytes(sv))
9
>>> bytes(sv)
b'f\x8c.\xba=&\xb4\x17='
>>> ShortVec2d.frombytes('f\x8c.\xba=&\xb4\x17=')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    ShortVec2d.frombytes('f\x8c.\xba=&\xb4\x17=')
  File "<pyshell#7>", line 24, in frombytes
    typecode = chr(octets[0])
TypeError: an integer is required (got type str)
>>> sv = ShortVec2d(3,4)
>>> bytes(sv)
b'f\x00\x00@@\x00\x00\x80@'
>>> ShortVec2d.frombytes('f\x00\x00@@\x00\x00\x80@')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ShortVec2d.frombytes('f\x00\x00@@\x00\x00\x80@')
  File "<pyshell#7>", line 24, in frombytes
    typecode = chr(octets[0])
TypeError: an integer is required (got type str)
>>> ShortVec2d.frombytes(b'f\x00\x00@@\x00\x00\x80@')
ShortVec2d(3.0,4.0)
>>> class Vectord2d:
	typecode = 'd'

	def __init__(self,x,y):
		self.__x = float(x)
		self.__y = float(y)
	def __iter__(self):
		return (i for i in (self.x,self.y))
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r},{!r})'.format(class_name,*self)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))
	def __eq__(self,other):
		return tuple(self) == tuple(other)
	def __abs__(self):
		return math.hypot(self.x,self.y)
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(*memv)
	def angle(self):
		return math.atan2(self.x,self.y)
	def __format__(self,fmt_spec = ''):
		if fmt_spec.endswith('p'):
			fmt_spec = fmt_spec[:-1]
			coords = (abs(self),self.angle())
			outer_fmt = '<{},{}>'
		else:
			coords = self
			outer_fmt = '({},{})'
		components = (format(c,fmt_spec) for c in coords)
		return outer_fmt.format(*components)
	@property
	def x(self):
		return self.__x
	@property
	def y(self):
		return self.__y
	def __iter__(self):
		return (i for i in (self.x,self.y))
	def __hash__(self):
		return hash(self.x)^hash(self.y)

	
>>> 
