import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index = [True, True, False])

#? print(df1.loc[True])

#       A  B  C
# True  1  4  7
# True  2  5  8

#? print(df1.iloc[1])

# A    2
# B    5
# C    8
# Name: True, dtype: int64