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

#? Creating a Dataframe from a Dictionary of lists

dict_list_dataFrame = pd.DataFrame({'Name':['Alex', 'Bob', 'Clarke'], 'Age':[20,22,23], 'Marks':[80,90,70]})
# print(dict_list_dataFrame)

#      Name  Age  Marks
# 0    Alex   20     80
# 1     Bob   22     90
# 2  Clarke   23     70

#? Creating a Dataframe from a Dictionary of Series

Name = pd.Series(['Alex', 'Bob', 'Clarke'])
English = pd.Series([80,90,70])
Math = pd.Series([90,80,70])
Chemistry = pd.Series([70,80,90])
Physics = pd.Series([70,90,80])
Ip = pd.Series([75,85,95])

dict_series_dataFrame = pd.DataFrame({'Name':Name, 'English':English, 'Math':Math, 'Chemistry':Chemistry, 'Physics':Physics, 'Ip':Ip})
# print(dict_series_dataFrame)

#      Name  English  Math  Chemistry  Physics  Ip
# 0    Alex       80    90         70       70  75
# 1     Bob       90    80         80       90  85
# 2  Clarke       70    70         90       80  95

#? Creating a DataFrame from a List of Dictionaries

student = [{'Name':'Alex', 'Age':20, 'Marks':80},{'Name':'Bob', 'Age':22, 'Marks':90},{'Name':'Clarke', 'Age':23, 'Marks':70}]
list_dict_dataFrame = pd.DataFrame(student)
# print(list_dict_dataFrame)

#      Name  Age  Marks
# 0    Alex   20     80
# 1     Bob   22     90
# 2  Clarke   23     70

#? Creating a DataFrame using Numpy array

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
columns = ['a','b','c']
index = ['row1','row2','row3']

array_DataFrame = pd.DataFrame(array, index = index, columns = columns)
# print(array_DataFrame)

#       a  b  c
# row1  1  2  3
# row2  4  5  6
# row3  7  8  9