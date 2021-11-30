n = int(input())
boxes = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i-1, -1, -1):
        if boxes[j] < boxes[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            
print(max(dp))