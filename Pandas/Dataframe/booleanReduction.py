import pandas as pd
import numpy as np

df = pd.DataFrame({'x':[]})

#? df.empty : if the df is empty
# print(df.empty) 

# True

df = pd.DataFrame({'X':[True, True], 'Y':[True, False], 'Z':[False, False]})
#? df.all() : True if all the values in the df are non-zero, non-empty or non-False
# print(df.all())

# X     True
# Y    False
# Z    False
# dtype: bool

#? df.any() : True if any of the values in the df are non-zero, non-empty or non-False
# print(df.any())

# X     True
# Y     True
# Z    False
# dtype: bool

#? even the head and tail function work to show the first or last n rows : default : n = 5 : format : df.head(n), df.tail(n)
