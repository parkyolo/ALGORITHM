import sys

def main():
    n = int(input())
    rgb = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(3)] for _ in range(n)] # dp[i][j] : i번째 집을 j색으로 칠하는 최소 비용
    answer = sys.maxsize
    
    for start in range(3):                                                      # 1. 시작 번호의 rgb값 고정
        for j in range(3):                                                      # 2. 첫 번째 집의 비용 초기화
            if start == j: dp[0][j] = rgb[0][j]
            else: dp[0][j] = sys.maxsize
        for i in range(1, n):
            for j in range(3):
                dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + rgb[i][j]  # 3. i-1번째 집을 j와 다른 두 색으로 칠한 비용 중 작은 값을 선택
        for end in range(3):
            if start == end: continue                                           # 4. 시작 번호와 끝 번호가 같으면 넘어감
            else:
                answer = min(answer, dp[-1][end])

    print(answer)

if __name__ == "__main__":
    main()