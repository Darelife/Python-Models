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

changingTheIndexSeries = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
changingTheIndexSeries.index = [x for x in "fghij"]

# print(changingTheIndexSeries)

# f    1
# g    2
# h    3
# i    4
# j    5
# dtype: int64

accessingValues = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])

# print(accessingValues["a"])
# 1

accessingAndSlicingValues = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
# print(accessingAndSlicingValues[0]) # 1
# print(accessingAndSlicingValues[0:3]) # 1, 2, 3
# print(accessingAndSlicingValues[0::2]) # 1, 3, 5
# print(accessingAndSlicingValues[-3:]) # 3, 4, 5

locSeries = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
# print(locSeries.loc['b':'e']) # 2, 3, 4, 5 
# b    2
# c    3
# d    4
# e    5
# dtype: int64
# loc is a method that allows you to access values by their index

ilocSeries = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
# print(ilocSeries.iloc[1:4]) # 2, 3, 4
# b    2
# c    3
# d    4
# iloc is a method that allows you to access values by their position
