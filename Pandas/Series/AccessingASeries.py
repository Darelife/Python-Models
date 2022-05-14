import pandas as pd
import numpy as np

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

headSeries = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
# To acess only the first n elements of the series: (default = 5)

# print(headSeries.head(3))

# a    1
# b    2
# c    3
# dtype: int64

tailSeries = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
# To acess only the last n elements of the series: (default = 5)

# print(tailSeries.tail(3))

# c    3
# d    4
# e    5
# dtype: int64