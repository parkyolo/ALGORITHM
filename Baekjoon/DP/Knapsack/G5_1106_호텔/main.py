import sys
INF = sys.maxsize

def main():
    c, n = map(int, input().split())
    info = list(list(map(int, input().split())) for _ in range(n)) # 홍보 비용, 늘어나는 고객 수
    dp = [INF for _ in range(1090)] # dp[i] : 고객을 i명 늘리기 위해 투자해야 하는 돈의 최솟값
    dp[0] = 0

    for cost, cnt in info:
        for i in range(cnt, 1090):
            dp[i] = min(dp[i], dp[i-cnt]+cost)
    
    print(min(dp[c:]))

if __name__ == "__main__":
    main()