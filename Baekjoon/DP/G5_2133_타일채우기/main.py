N = int(input())
dp = [0 for _ in range(31)]
dp[0] = 1

if N%2: # N이 홀수일 때
    print(0)
    exit()

for i in range(2, N+1, 2):
    dp[i] += dp[i-2] * 3
    for j in range(0, i-3, 2):
        dp[i] += dp[j] * 2

print(dp[N])