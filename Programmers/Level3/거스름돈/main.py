def solution(n, money):
    dp = [0 for _ in range(n)]
    dp = [1] + dp
    for i in range(len(money)):
        for j in range(money[i], n+1):
            dp[j] += dp[j - money[i]] 
    
    # dp[1] += dp[0] 1
    # dp[2] += dp[1] 1
    # dp[3] += dp[2] 1
    # dp[4] += dp[3] 1
    # dp[5] += dp[4] 1
    # dp[2] += dp[0] 1+1
    # dp[3] += dp[1] 1+1
    # dp[4] += dp[2] 1+2
    # dp[5] += dp[3] 1+2
    # dp[5] += dp[0] 3+1
    # dp = [1, 1, 2, 2, 3, 4]

    return dp[n]

print(solution(5, [1, 2, 5]), 4)