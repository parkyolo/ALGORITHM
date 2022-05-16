dp = [0, 1, 2, 4]
T = int(input())
for _ in range(T):
    N = int(input())
    if len(dp) < N+1:
        for i in range(len(dp), N+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[N])