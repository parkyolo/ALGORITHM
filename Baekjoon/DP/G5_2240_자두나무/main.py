T, W = map(int, input().split())
plums = [0]+[int(input()) for _ in range(T)]

dp = [[0 for _ in range(W+1)] for _ in range(T+1)] # dp[i][j] : i초 지났고 j번 움직였을 때 먹은 자두의 최대 개수

for i in range(1, T+1):
    if plums[i] == 1: # 한 번도 움직이지 않은 경우
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, min(i+1, W+1)): # 1번 이상 움직인 경우
        if (plums[i] == 1 and j % 2 == 0) or (plums[i] == 2 and j % 2 == 1): # 자두를 먹을 때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        else: # 자두를 안먹을 때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[T]))