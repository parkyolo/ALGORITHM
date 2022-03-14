n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [[0 for _ in range(101)] for _ in range(n)]

for i in range(n):
    for j in range(100, 0, -1):
        if j > L[i]:
            # max( i번 사람까지 인사했을 때의 기쁨, i-1번 사람까지 인사했을 때의 기쁨 )
            dp[i][j] = max(dp[i - 1][j - L[i]] + J[i], dp[i - 1][j])
        else:
            # i번 사람과 인사하지 못할 때
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])