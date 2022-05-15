import pandas as pd
import numpy as np

student = {'Name':['Alex', 'Bob', 'Clarke'], 'Age':[20,22,23], 'Marks':[80,90,70]}
dataFrame = pd.DataFrame(student)
#? Regular
# print(dataFrame) 

#      Name  Age  Marks
# 0    Alex   20     80
# 1     Bob   22     90
# 2  Clarke   23     70

dataFrame.index = ([3,4,5])
# print(dataFrame) # To Change the index of the DataFrame

#      Name  Age  Marks
# 3    Alex   20     80
# 4     Bob   22     90
# 5  Clarke   23     70

dataFrame.set_index('Name', inplace=True) # To change the index of the DataFrame to a column
# print(dataFrame)

#         Age  Marks
# Name
# Alex     20     80
# Bob      22     90
# Clarke   23     70

dataFrame.reset_index(inplace=True) # To reset the index of the DataFrame
# print(dataFrame)

#      Name  Age  Marks
# 0    Alex   20     80
# 1     Bob   22     90
# 2  Clarke   23     70
