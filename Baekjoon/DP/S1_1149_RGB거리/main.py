n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n)]

for j in range(3):
    dp[0][j] = rgb[0][j]

for i in range(1, n):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + rgb[i][j]

print(min(dp[-1]))