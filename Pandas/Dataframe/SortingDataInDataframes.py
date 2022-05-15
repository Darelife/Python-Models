import pandas as pd
import numpy as np

Student_marks = pd.Series({'Alex':80,'Bob':90,'Clarke':70})
Student_age = pd.Series({'Alex':20,'Bob':22,'Clarke':23})

studentDataFrame = pd.DataFrame({'Marks':Student_marks,'Age':Student_age})
#? print(studentDataFrame)

#         Marks  Age
# Alex       80   20
# Bob        90   22
# Clarke     70   23

#? print(studentDataFrame.sort_values(by=['Marks'])) # Ascending | sort by the values in the column 'Marks'

#         Marks  Age
# Clarke     70   23
# Alex       80   20
# Bob        90   22

#? print(studentDataFrame.sort_values(by=['Marks'],
#? ascending=False)) # Descending | sort by the values in the column 'Age'

#         Marks  Age
# Bob        90   22
# Alex       80   20
# Clarke     70   23
