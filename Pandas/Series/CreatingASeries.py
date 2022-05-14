import pandas as pd
import numpy as np

simpleSeriies = pd.Series([1, 2, 3, 4, 5], index=["one", "two", "three", "four", "five"])
#print(simpleSeriies)

# one      1
# two      2
# three    3
# four     4
# five     5
# dtype: int64

forloopIndexSeries = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
# print(forloopIndexSeries)

# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64

missingValuesSeries = pd.Series([7.5, 5.4, np.NaN, -34.5], index=[x for x in ["a", "b", "c", "d"]])
#np.NaN is a special numpy value that represents "not a number"

# print(missingValuesSeries)

# a     7.5
# b     5.4
# c     NaN
# d   -34.5
# dtype: float64

constant_value_series = pd.Series(5, index=[x for x in "abcde"])
# print(constant_value_series)

# a    5
# b    5
# c    5
# d    5
# e    5
# dtype: int64

series_from_dict = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
# print(series_from_dict)

# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64

series1 = np.arange(10,15)
series_from_math = pd.Series(data = series1**2, index = series1) 
#there's also no need to write "data ="
# print(series_from_math)

# 10    100
# 11    121
# 12    144
# 13    169
# 14    196
# dtype: int32

array1 = np.array([10,20,30,40,50])
series_from_np_array = pd.Series(array1, index = ["a", "b", "c", "d", "e"])
# print(series_from_np_array)

# a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int32