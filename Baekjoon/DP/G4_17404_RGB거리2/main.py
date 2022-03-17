import sys
n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n)]
answer = sys.maxsize
for start in range(3):
    for j in range(3): # 시작 번호의 rgb값 고정
        if start == j: dp[0][j] = rgb[0][j]
        else: dp[0][j] = sys.maxsize
    for i in range(1,n):
        for j in range(3):
            dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + rgb[i][j]
    for end in range(3):
        if start == end: continue # 시작 번호와 끝 번호가 같으면 continue
        else:
            answer = min(answer, dp[-1][end])

print(answer)