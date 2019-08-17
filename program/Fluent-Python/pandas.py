Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> from pandas import Series,DataFrame
>>> s = Series(data = [120,136,128,99],index = ['Ma','Python','En','Chinese'])
>>> s
Ma         120
Python     136
En         128
Chinese     99
dtype: int64
>>> s.shape
(4,)
>>> v = s.values
>>> v
array([120, 136, 128,  99], dtype=int64)
>>> type(v)
<class 'numpy.ndarray'>
>>> s.mean()
120.75
>>> s.max()
136
>>> s.std()
15.903353943953666
>>> s.pow(2)
Ma         14400
Python     18496
En         16384
Chinese     9801
dtype: int64
>>> help(s.std)
Help on method std in module pandas.core.series:

std(axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs) method of pandas.core.series.Series instance
    Return sample standard deviation over requested axis.
    
    Normalized by N-1 by default. This can be changed using the ddof argument
    
    Parameters
    ----------
    axis : {index (0)}
    skipna : boolean, default True
        Exclude NA/null values. If an entire row/column is NA, the result
        will be NA
    level : int or level name, default None
        If the axis is a MultiIndex (hierarchical), count along a
        particular level, collapsing into a scalar
    ddof : int, default 1
        Delta Degrees of Freedom. The divisor used in calculations is N - ddof,
        where N represents the number of elements.
    numeric_only : boolean, default None
        Include only float, int, boolean columns. If None, will attempt to use
        everything, then use only numeric data. Not implemented for Series.
    
    Returns
    -------
    std : scalar or Series (if level specified)

>>> df = DataFrame(data = mp.random.randint(0,150,size = (10,3)),index = list('abcdefhijk'),columns = ['Python','En','Math'])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df = DataFrame(data = mp.random.randint(0,150,size = (10,3)),index = list('abcdefhijk'),columns = ['Python','En','Math'])
NameError: name 'mp' is not defined
>>> df = DataFrame(data = np.random.randint(0,150,size = (10,3)),index = list('abcdefhijk'),columns = ['Python','En','Math'])
>>> df
   Python   En  Math
a     122   19    17
b     148    2    81
c     122    9   118
d      25   44    32
e     121  101    63
f     128  124   140
h      93   50    98
i     109   89    34
j       1   54     7
k      35  112     9
>>> df.shape
(10, 3)
>>> v = df.values
>>> v
array([[122,  19,  17],
       [148,   2,  81],
       [122,   9, 118],
       [ 25,  44,  32],
       [121, 101,  63],
       [128, 124, 140],
       [ 93,  50,  98],
       [109,  89,  34],
       [  1,  54,   7],
       [ 35, 112,   9]])
>>> df.mean()
Python    90.4
En        60.4
Math      59.9
dtype: float64
>>> df.mean(axis=0)
Python    90.4
En        60.4
Math      59.9
dtype: float64
>>> df.mean(axis=1)
a     52.666667
b     77.000000
c     83.000000
d     33.666667
e     95.000000
f    130.666667
h     80.333333
i     77.333333
j     20.666667
k     52.000000
dtype: float64
>>> 
