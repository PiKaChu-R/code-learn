Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> from pandas import Series, DataFrame
>>> s = Series(np.random.randint(0,150,size =100),index=np.arange(10,110),dtype=np.int16,name='python')
>>> s
10     104
11      96
12      28
13      55
14      87
15     103
16      82
17      57
18      47
19     110
20     113
21      19
22     142
23      48
24      16
25      22
26      27
27       9
28       3
29      11
30      92
31      84
32       7
33      11
34      15
35      16
36     100
37     103
38       8
39     117
      ... 
80      49
81      36
82     140
83      18
84     109
85      59
86      66
87      72
88      28
89       6
90      68
91      85
92     139
93     126
94     112
95      66
96     148
97      37
98     134
99       6
100     76
101    103
102    116
103     70
104    145
105     96
106     86
107    105
108     11
109     65
Name: python, Length: 100, dtype: int16
>>> type(s)
<class 'pandas.core.series.Series'>
>>> s[[10,20]]
10    104
20    113
Name: python, dtype: int16
>>> s[10:20]
20    113
21     19
22    142
23     48
24     16
25     22
26     27
27      9
28      3
29     11
Name: python, dtype: int16
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[0]
  File "C:\Users\zfr_Rambo\AppData\Roaming\Python\Python36\site-packages\pandas\core\series.py", line 868, in __getitem__
    result = self.index.get_value(self, key)
  File "C:\Users\zfr_Rambo\AppData\Roaming\Python\Python36\site-packages\pandas\core\indexes\base.py", line 4375, in get_value
    tz=getattr(series.dtype, 'tz', None))
  File "pandas\_libs\index.pyx", line 81, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 89, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 987, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 993, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 0
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[1]
  File "C:\Users\zfr_Rambo\AppData\Roaming\Python\Python36\site-packages\pandas\core\series.py", line 868, in __getitem__
    result = self.index.get_value(self, key)
  File "C:\Users\zfr_Rambo\AppData\Roaming\Python\Python36\site-packages\pandas\core\indexes\base.py", line 4375, in get_value
    tz=getattr(series.dtype, 'tz', None))
  File "pandas\_libs\index.pyx", line 81, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 89, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 987, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 993, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 1
>>> s[9]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s[9]
  File "C:\Users\zfr_Rambo\AppData\Roaming\Python\Python36\site-packages\pandas\core\series.py", line 868, in __getitem__
    result = self.index.get_value(self, key)
  File "C:\Users\zfr_Rambo\AppData\Roaming\Python\Python36\site-packages\pandas\core\indexes\base.py", line 4375, in get_value
    tz=getattr(series.dtype, 'tz', None))
  File "pandas\_libs\index.pyx", line 81, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 89, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 987, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 993, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 9
>>> s[10]
104
>>> s[::2]
10     104
12      28
14      87
16      82
18      47
20     113
22     142
24      16
26      27
28       3
30      92
32       7
34      15
36     100
38       8
40     124
42      24
44     111
46     102
48       8
50     144
52      55
54      20
56      84
58     131
60      96
62      64
64      72
66      34
68     144
70       7
72     103
74      70
76     121
78       0
80      49
82     140
84     109
86      66
88      28
90      68
92     139
94     112
96     148
98     134
100     76
102    116
104    145
106     86
108     11
Name: python, dtype: int16
>>> s.loc[10]
104
>>> s.index
Int64Index([ 10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,
             23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,
             36,  37,  38,  39,  40,  41,  42,  43,  44,  45,  46,  47,  48,
             49,  50,  51,  52,  53,  54,  55,  56,  57,  58,  59,  60,  61,
             62,  63,  64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,
             75,  76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,  87,
             88,  89,  90,  91,  92,  93,  94,  95,  96,  97,  98,  99, 100,
            101, 102, 103, 104, 105, 106, 107, 108, 109],
           dtype='int64')
>>> df = DataFrame(data = np.random.randint(0,150,size=(10,3)),index = list('ABCDEFHIJK'),columns=['Python','En','Math'])
>>> df
   Python   En  Math
A       7  102   110
B      33   49    60
C      70    2    95
D     124   80     0
E      56   64   146
F      20   29   112
H      68  112   104
I      50   44    67
J      19  129   136
K      22   87    58
>>> df['A']
Traceback (most recent call last):
  File "C:\Users\zfr_Rambo\AppData\Roaming\Python\Python36\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'A'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    df['A']
  File "C:\Users\zfr_Rambo\AppData\Roaming\Python\Python36\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\zfr_Rambo\AppData\Roaming\Python\Python36\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'A'
>>> df['Python':'Math']
Empty DataFrame
Columns: [Python, En, Math]
Index: []
>>> df[['Python','Math']]
   Python  Math
A       7   110
B      33    60
C      70    95
D     124     0
E      56   146
F      20   112
H      68   104
I      50    67
J      19   136
K      22    58
>>> df.iloc[0]
Python      7
En        102
Math      110
Name: A, dtype: int32
>>> df.iloc[2]
Python    70
En         2
Math      95
Name: C, dtype: int32
>>> 
