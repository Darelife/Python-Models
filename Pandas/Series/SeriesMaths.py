import pandas as pd
import numpy as np

# Index needs to be the same for both the series
# If the index is different, it will return "NaN", which means "Not a Number" as the values, and it will add the index values

# Same Index
series1 = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
series2 = pd.Series([11, 12, 13, 14, 15], index=["a", "b", "c", "d", "e"])
# You can do +,-,*,/,//,**,%
# You can also add, subtract, multiply, divide, floor divide, and exponentiate, etc with NUMBERS too.
# print(series1 + series2) # It will add the values of both the series'

# a    12
# b    14
# c    16
# d    18
# e    20
# dtype: int64

# Different Index
series3 = pd.Series([21, 22, 23, 24, 25], index=["aa", "bb", "cc", "dd", "ee"])
series4 = pd.Series([31, 32, 33, 34, 35], index=["1a1", "2b2", "3c3", "4d4", "5e5"])

# print(series3 + series4)

# 1a1   NaN
# 2b2   NaN
# 3c3   NaN
# 4d4   NaN
# 5e5   NaN
# aa    NaN
# bb    NaN
# cc    NaN
# dd    NaN
# ee    NaN
# dtype: float64