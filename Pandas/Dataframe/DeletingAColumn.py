import pandas as pd
import numpy as np

student = {'Name':['Alex', 'Bob', 'Clarke'], 'Age':[20,22,23], 'Marks':[80,90,70]}
dataFrame = pd.DataFrame(student)

# using the del keyword : del dataFrame['average']
i = dataFrame.pop('Age')
#? print(i)

# 0    20
# 1    22
# 2    23
# Name: Age, dtype: int64

#? print(dataFrame)

#      Name  Marks
# 0    Alex     80
# 1     Bob     90
# 2  Clarke     70

dataFrame.drop('Marks', axis=1, inplace=True)
# print(dataFrame)

#      Name
# 0    Alex
# 1     Bob
# 2  Clarke

student = {'Name':['Alex', 'Bob', 'Clarke'], 'Age':[20,22,23], 'Marks':[80,90,70]}
dataFrame = pd.DataFrame(student)