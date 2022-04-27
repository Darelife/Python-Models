import pandas as pd
import numpy as np

changingTheIndexSeries = pd.Series([1, 2, 3, 4, 5], index=[x for x in "abcde"])
changingTheIndexSeries.index = [x for x in "fghij"]

# print(changingTheIndexSeries)

# f    1
# g    2
# h    3
# i    4
# j    5
# dtype: int64