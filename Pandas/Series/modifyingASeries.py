import pandas as pd
import numpy as np

changingTheIndexSeries = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
changingTheIndexSeries.index = [x for x in "fghij"]
# print(changingTheIndexSeries)

# f    1
# g    2
# h    3
# i    4
# j    5
# dtype: int64

namingASeries = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
namingASeries.name = "my_series"
# print(namingASeries)

# a    1
# b    2
# c    3
# d    4
# e    5
# Name: my_series, dtype: int64

dropSeriesValue = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
dropSeriesValue.drop("a", inplace=True) # drop the value at index "a"
# print(dropSeriesValue)

# b    2
# c    3
# d    4
# e    5
# dtype: int64