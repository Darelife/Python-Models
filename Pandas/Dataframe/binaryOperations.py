import pandas as pd
import numpy as np

dataFrame1 = pd.DataFrame({'Age':[20,22,23]})
dataFrame2 = pd.DataFrame({'Age':[80,90,70]})

sub = dataFrame1.sub(dataFrame2) # DataFrame 1 - DataFrame 2
add = dataFrame1.add(dataFrame2) # DataFrame 1 + DataFrame 2
mul = dataFrame1.mul(dataFrame2) # DataFrame 1 * DataFrame 2
div = dataFrame1.div(dataFrame2) # DataFrame 1 / DataFrame 2
rsub = dataFrame1.rsub(dataFrame2) # DataFrame 2 - DataFrame 1
radd = dataFrame1.radd(dataFrame2) # DataFrame 2 + DataFrame 1

# print(sub)
#    Age
# 0  -60
# 1  -68
# 2  -47

# print(add)
#    Age
# 0  120
# 1  210
# 2  170

# print(mul)
#    Age
# 0  160
# 1  300
# 2  140

#print(div)
#    Age
# 0  0.2
# 1  0.3
# 2  0.2

#print(rsub)
#    Age
# 0  -60
# 1  -68
# 2  -47

#print(radd)
#    Age
# 0  120
# 1  210
# 2  170

# You can also do dataFrame1 + dataFrame2, or dataFrame1 + 50, etc.

# print(dataFrame1 == dataFrame2) # you can do >, >=, <, <=, ==, !=, etc.

#      Age
# 0  False
# 1  False
# 2  False