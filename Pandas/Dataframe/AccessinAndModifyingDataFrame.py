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

dataFrame.loc[3] = ['May',20,80] # To add a new row with index 3
# print(dataFrame)

#      Name  Age  Marks
# 0    Alex   20     80
# 1     Bob   22     90
# 2  Clarke   23     70
# 3     May   20     80

dataFrame.loc[2] = ['Clarissa',21,79] # To update the values in the row with index 2
# print(dataFrame)

#        Name  Age  Marks
# 0      Alex   20     80
# 1       Bob   22     90
# 2  Clarissa   21     79
# 3       May   20     80

#? Renaming a column
dataFrame.columns = ['Student_Name', 'Age', 'Marks']
# OR
# dataFrame.rename(columns={'Name':'Student_Name'}, inplace=True)
# print(dataFrame)

#   Student_Name  Age  Marks
# 0        Alex   20     80
# 1         Bob   22     90
# 2    Clarissa   21     79
# 3         May   20     80

#? Adding a new column
dataFrame['Grade'] = dataFrame['Marks']/10
# print(dataFrame)

#   Student_Name  Age  Marks  Grade
# 0         Alex   20     80    8.0
# 1          Bob   22     90    9.0
# 2     Clarissa   21     79    7.9
# 3          May   20     80    8.0

#? Selecting a specific column
# print(dataFrame['Student_Name'])

# 0        Alex
# 1         Bob
# 2    Clarissa
# 3         May
# Name: Student_Name, dtype: object

#? iloc

# print(dataFrame)

#   Student_Name  Age  Marks  Grade
# 0         Alex   20     80    8.0
# 1          Bob   22     90    9.0
# 2     Clarissa   21     79    7.9
# 3          May   20     80    8.0

# print(dataFrame.iloc[1:3, 0:2]) # To select a specific row [1:3] and column [0:2]

#   Student_Name  Age
# 1          Bob   22
# 2     Clarissa   21

