import pandas as pd
import numpy as np

set = ([[2,3,4], [8], [9,10]])
df = pd.DataFrame(set)
# print(df)

#    0     1    2
# 0  2   3.0  4.0
# 1  8   NaN  NaN
# 2  9  10.0  NaN

df = (df.fillna(0)) # Fill all NaN values with 0
# print(df)

#    0     1    2
# 0  2   3.0  4.0
# 1  8   0.0  0.0
# 2  9  10.0  0.0

set = ([[2,3,4], [8], [9,10]])
df = pd.DataFrame(set)
df.fillna({0:-8, 1:-10, 2:-5}, inplace = True) # Fill all NaN values with -8, -10, -5 for the rows 0, 1, 2
# print(df)

#? fflil
set = ([[2,3,4], [8], [9,10]])
df = pd.DataFrame(set)
df.fillna(method = 'ffill', inplace=True) # Fill all NaN values with the previous value
# print(df)
#? inplace just means that the changes are made in the original DataFrame