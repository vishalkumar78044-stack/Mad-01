# import pandas as pd
# import os

# folder = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(folder, "data.csv")

# dp = pd.read_csv("data.csv")
# print(dp[dp["Course id"] == 2001])
# print(dp[dp[" Course id"] == 2001][" Marks"].max())
# dp = pd.read_csv("data.csv")
# print(dp)
# print(dp.columns[1])
# daa = (dp[dp["Student id"] == 1001].values.tolist())
# print(daa)
# for i in daa:
#     print(i[1])

a = [[1,2,3],[2,3,4],[3,4,5]]
print(sum([i[1] for i in a]))













