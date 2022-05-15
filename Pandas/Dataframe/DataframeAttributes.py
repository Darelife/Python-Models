import pandas as pd
import numpy as np

sampleDataframe = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
# print(sampleDataframe)

#         one       two     three
# a  0.006236  0.323874  0.198039
# c  0.829182  0.479661  0.722509
# e  1.621526 -0.838284 -1.030303
# f -0.880257 -1.852701 -1.218998
# h -1.973476 -0.073572 -0.610535

#? sampleDataframe.index
# print(sampleDataframe.index)

# Index(['a', 'c', 'e', 'f', 'h'], dtype='object')

#? sampleDataframe.columns
# print(sampleDataframe.columns)

# Index(['one', 'two', 'three'], dtype='object')

#? sampleDataframe.axes
# print(sampleDataframe.axes)

# [Index(['a', 'c', 'e', 'f', 'h'], dtype='object'), Index(['one', 'two', 'three'], dtype='object')]

#? sampleDataframe.dtypes
# print(sampleDataframe.dtypes)

# one      float64
# two      float64
# three    float64
# dtype: object

#? sampleDataframe.size
# print(sampleDataframe.size)

# 15

#? sampleDataframe.shape
# print(sampleDataframe.shape)

# (5, 3)

#? sampleDataframe.ndim # dimension of the data = 2D for dataframe = 2
# print(sampleDataframe.ndim)

# 2

#? sampleDataframe.values
# print(sampleDataframe.values)

# [[-1.12020648 -0.97901643  0.65596681]
#  [-0.82619236  0.97360477 -0.43332864]
#  [-0.70724586  1.284933   -0.70347142]
#  [-0.9236861  -0.90559838  0.48508272]
#  [ 0.78208081  1.81636173 -0.096863  ]]

#? sampleDataframe.empty
# print(sampleDataframe.empty) # If the dataframe is empty, it will return True

# False
student_age = pd.Series({'Tom': pd.NA, 'Jack': 18, 'John': 20, 'Jill': 25})
dataFrame2 = pd.DataFrame({'Age':student_age})
# print(dataFrame2)
# print(dataFrame2.empty)
# False

#? sampleDataframe.isna()
# print(sampleDataframe.isna())

#      one    two  three
# a  False  False  False
# c  False  False  False
# e  False  False  False
# f  False  False  False
# h  False  False  False

# print(dataFrame2.isna())

#         Age
# Tom    True
# Jack  False
# John  False
# Jill  False

#? dataFrame2.notna()
# print(dataFrame2.notna())

#         Age
# Tom   False
# Jack   True
# John   True
# Jill   True

#? sampleDataFrame.count()
# 0 -> Default -> Rows
# 1 -> Columns

# print(sampleDataframe.count()) # Rows

# one      5
# two      5
# three    5
# dtype: int64

# print(sampleDataframe.count(axis=1)) # count the number of non-NA values in each column
# Or, print(sampleDataframe.count(axis='columns'))
# Or, print(sampleDataframe.count(1))

# a    3
# c    3
# e    3
# f    3
# h    3
# dtype: int64

#? sampleDataframe.T # Converts the rows and columns of the dataframe to columns and rows
# print(sampleDataframe.T)

#               a         c         e         f         h
# one    0.013728 -0.127090  2.087969  0.605054  0.525910
# two   -0.700947  0.784680  2.057025 -0.248225 -0.099421
# three  0.679052 -1.499611  1.566669  1.134924 -0.098658