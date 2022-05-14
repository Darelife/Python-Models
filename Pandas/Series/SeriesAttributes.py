import pandas as pd
import numpy as np

series = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
series.name = "Dummy Series"
# print(series)

# a    1
# b    2
# c    3
# d    4
# e    5
# Name: Dummy Series, dtype: int64

#? series.index
# print(series.index)
# Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

#? series.index.name
# series.index.name = "Dummy Index"
# print(series.index.name)
# Dummy Index

#? series.values
# print(series.values)
#[1 2 3 4 5]

#? series.dtype
# print(series.dtype)
# int64

#? series.shape
# print(series.shape)
# (5,)

#? series.nbytes
# print(series.nbytes) #number of bytes in the memory occupied by the series
# 40

#? series.ndim
# print(series.ndim) #number of dimensions of the series
# 1 #the dimension of a series is 1D

#? series.size
# print(series.size) #number of elements in the series
# 5

#? series.items
# print(series.items) #returns a list of tuples of the index and values

# <bound method Series.items of 
# a    1
# b    2
# c    3
# d    4
# e    5
# Name: Dummy Series, dtype: int64>

#? series.itemsize
# print(series.itemsize)
# 8
# Many new versions have removed this attribute, cuz it's not useful anymore. It always shows the size 
# of the items in the series. In Pandas, it's always 8 bytes.

#? series.hasnans
# print(series.hasnans) #returns True if there are NaN values in the series
# False

#? series.empty
# print(series.empty) #returns True if the series is empty
# False