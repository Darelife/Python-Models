import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index = [4,9,6])
df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60], 'C': [70, 80, 90]}, index = [4,7,6])

df3 = pd.concat([df1, df2], axis = 0)
# print(df3)

#     A   B   C
# 4   1   4   7
# 9   2   5   8
# 6   3   6   9
# 4  10  40  70
# 7  20  50  80
# 6  30  60  90

df4 = pd.concat([df1, df2], axis = 1)
# print(df4)

#      A    B    C     A     B     C
# 4  1.0  4.0  7.0  10.0  40.0  70.0
# 6  3.0  6.0  9.0  30.0  60.0  90.0
# 7  NaN  NaN  NaN  20.0  50.0  80.0
# 9  2.0  5.0  8.0   NaN   NaN   NaN

# join = 'inner' -> intersection, outer -> union
df5 = pd.concat([df1, df2], axis = 0, ignore_index = True, join='inner')
# print(df5)

#     A   B   C
# 0   1   4   7
# 1   2   5   8
# 2   3   6   9
# 3  10  40  70
# 4  20  50  80
# 5  30  60  90

df6 = pd.concat([df1, df2], axis = 1, ignore_index = True, join='inner')
# print(df6)

#    0  1  2   3   4   5
# 4  1  4  7  10  40  70
# 6  3  6  9  30  60  90