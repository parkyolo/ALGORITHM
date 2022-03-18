n = int(input())
dp = [-1 for _ in range(n+1)] # 0은 상근, 1은 창영

stone = [1,3,4]
for i in range(1, n+1):
    if i in stone: dp[i] = 0
    else:
        CY = False # 이전 경우의 수 창영이가 이기는 경우가 있는지
        for st in stone:
            if i-st > 0:
                if dp[i-st]: CY = True
        if CY: dp[i] = 0
        else: dp[i] = 1

print("CY" if dp[n] else "SK")