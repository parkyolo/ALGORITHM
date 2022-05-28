import sys

n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 1

for i in range(2, n+1):
    min_ = sys.maxsize
    for j in range(1, int(i**0.5)+1):
        min_ = min(min_, dp[i-j**2])
    dp[i] = min_ + 1

# print(dp)
print(dp[n])