n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))
dp = [0 for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[0] = stairs[0]
    elif i == 1:
        dp[1] = max(stairs[1], stairs[0]+stairs[1])
    elif i == 2:
        dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    else:
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
print(dp[-1])