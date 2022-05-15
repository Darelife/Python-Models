import pandas as pd
import numpy as np

#? Creating a Dataframe from a List
#* Single Column DataFrame

data = [10,20,30,40,50]
index = ["a","b","c","d","e"]
columns = ["col1"]
listDataFrame = pd.DataFrame(data, index = index, columns = columns)
# print(listDataFrame)

#    col1
# a    10
# b    20
# c    30
# d    40
# e    50

#* Multiple Column DataFrame

data = [['Alex',10],['Bob',12],['Clarke',13]]
listDataFrame = pd.DataFrame(data, columns = ["Name","Age"], index = ["Sr.No1","Sr.No2","Sr.No3"])
# print(listDataFrame)

#           Name  Age
# Sr.No1    Alex   10
# Sr.No2     Bob   12
# Sr.No3  Clarke   13

#? Creating a Dataframe from a Series

Student_marks = pd.Series({'Alex':80,'Bob':90,'Clarke':70})
Student_age = pd.Series({'Alex':20,'Bob':22,'Clarke':23})

seriesDataFrame = pd.DataFrame({'Marks':Student_marks,'Age':Student_age})
# print(seriesDataFrame)

#         Marks  Age
# Alex       80   20
# Bob        90   22
# Clarke     70   23