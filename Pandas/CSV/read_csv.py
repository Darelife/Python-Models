import pandas as pd
import numpy as np

df = pd.read_csv("Pandas\CSV\csv_file.csv")
# print(df)

#    Empid     Name  Rating
# 0      1   Ritesh       5
# 1      2   Aakash       7

df2 = pd.read_csv("Pandas\CSV\csv_file.csv", usecols = ['Empid', 'Rating'])
# print(df2)

#    Empid  Rating
# 0      1       5
# 1      2       7

df3 = pd.read_csv("Pandas\CSV\csv_file.csv", nrows = 1) #only read the first row
# print(df3)

#    Empid    Name  Rating
# 0      1  Ritesh       5

df4 = pd.read_csv("Pandas\CSV\csv_file.csv", index_col=0)
# print(df4)

#           Name  Rating
# Empid
# 1       Ritesh       5
# 2       Aakash       7

df5 = pd.read_csv("Pandas\CSV\csv_file.csv", index_col=1)
# print(df5)

#          Empid  Rating
# Name
# Ritesh       1       5
#  Aakash      2       7

df6 = pd.read_csv("Pandas\CSV\csv_file.csv", skiprows=1)
# print(df6)

#    1   Ritesh   5
# 0  2   Aakash   7

df7 = pd.read_csv("Pandas\CSV\csv_file.csv", header=None)
# print(df7)

#        0        1       2
# 0  Empid     Name  Rating
# 1      1   Ritesh       5
# 2      2   Aakash       7

df8 = pd.read_csv("Pandas\CSV\csv_file.csv", header = 0)
# print(df8)

#    Empid     Name  Rating
# 0      1   Ritesh       5
# 1      2   Aakash       7

df9 = pd.read_csv("Pandas\CSV\csv_file.csv", header = 1)
# print(df9)

#    1   Ritesh   5
# 0  2   Aakash   7

df10 = pd.read_csv("Pandas\CSV\csv_file.csv", na_values=[5, 7]) #Converts 5 and 7 to NaN
# print(df10)

#    Empid     Name  Rating
# 0      1   Ritesh     NaN
# 1      2   Aakash     NaN

