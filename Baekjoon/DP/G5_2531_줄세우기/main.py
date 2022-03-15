n = int(input())
line = [int(input())]
dp = [1 for _ in range(n)]
for i in range(1, n):
    line.append(int(input()))
    for j in range(i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))