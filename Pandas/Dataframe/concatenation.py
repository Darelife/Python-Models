import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60], 'C': [70, 80, 90]})

df3 = pd.concat([df1, df2], axis = 0)
# print(df3)

#     A   B   C
# 0   1   4   7
# 1   2   5   8
# 2   3   6   9
# 0  10  40  70
# 1  20  50  80
# 2  30  60  90

df4 = pd.concat([df1, df2], axis = 1)
# print(df4)

#    A  B  C   A   B   C
# 0  1  4  7  10  40  70
# 1  2  5  8  20  50  80
# 2  3  6  9  30  60  90