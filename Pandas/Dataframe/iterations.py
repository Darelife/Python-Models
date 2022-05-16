import pandas as pd
import numpy as np

student = {'Name':['Alex', 'Bob', 'Clarke'], 'Age':[20,22,23], 'Marks':[80,90,70]}
dataFrame = pd.DataFrame(student)

for (row, rowSeries) in dataFrame.iterrows():
    # print("Row Name : ", row)
    # print("Row Data : \n", rowSeries)
    pass

# Row Name :  0
# Row Data :
#  Name     Alex
# Age        20
# Marks      80
# Name: 0, dtype: object
# Row Name :  1
# Row Data :
#  Name     Bob
# Age       22
# Marks     90
# Name: 1, dtype: object
# Row Name :  2
# Row Data :
#  Name     Clarke
# Age          23
# Marks        70
# Name: 2, dtype: object

for (column, columnSeries) in dataFrame.iteritems():
    # print("Column Name : ", column)
    # print("Column Data : \n", columnSeries)
    pass

# Column Name :  Name
# Column Data :
#  0      Alex
# 1       Bob
# 2    Clarke
# Name: Name, dtype: object
# Column Name :  Age
# Column Data :
#  0    20
# 1    22
# 2    23
# Name: Age, dtype: int64
# Column Name :  Marks
# Column Data :
#  0    80
# 1    90
# 2    70
# Name: Marks, dtype: int64