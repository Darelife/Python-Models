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

