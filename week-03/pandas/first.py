import pandas as pd

dp = pd.read_csv("data.csv")
# print(dp[dp["Student id"]==1001]["Marks"].sum())
print(dp)

print("vishal")

dp = pd.read_csv("data.csv")
print(dp[dp["Course id"]==2001]["Marks"].sum())