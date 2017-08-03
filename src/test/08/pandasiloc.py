import pandas as pd
import numpy as np

data = [[1,1],[2,2],[3,3],[4,4]]
# index = ['d','e']
columns=['a','b']
# df = pd.DataFrame(data=data, index=index, columns=columns)
df = pd.DataFrame(data=data, columns=columns)
print(df)
print(df.iloc[np.random.permutation(4)])
print(df.iloc[np.random.permutation(4)].reset_index(drop=True))

#    a  b
# 0  1  1
# 1  2  2
# 2  3  3
# 3  4  4
#    a  b
# 2  3  3
# 0  1  1
# 3  4  4
# 1  2  2
#    a  b
# 0  3  3
# 1  1  1
# 2  4  4
# 3  2  2