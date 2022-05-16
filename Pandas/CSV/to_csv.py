import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df.to_csv("Pandas\\CSV\\to_csv.csv")

df2 = pd.read_csv("Pandas\\CSV\\to_csv.csv")
# print(df2)

#    Unnamed: 0  A  B  C
# 0           0  1  4  7
# 1           1  2  5  8
# 2           2  3  6  9

df3 = pd.read_csv("Pandas\\CSV\\to_csv.csv", index_col = 0)
# print(df3)

#    A  B  C
# 0  1  4  7
# 1  2  5  8
# 2  3  6  9

df4 = pd.read_csv("Pandas\\CSV\\csv_file.csv")
df5 = df4.to_csv("Pandas\\CSV\\to_csv2.csv", columns=["Empid", "Name"])