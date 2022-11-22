def main():
    n = int(input())
    matrix = list(list(map(int, input().split())) for _ in range(n))
    dp = [[2**31 for _ in range(n)] for _ in range(n)]  # dp[i][j]: i번째 행렬과 j번째 행렬을 곱하는 데 필요한 곱셈의 최소 횟수
    
    for i in range(n):
        dp[i][i] = 0    # 자기자신과의 곱은 0
        if i < n-1: dp[i][i+1] = matrix[i][0] * matrix[i][1] * matrix[i+1][1]   # i부터 i+1까지의 곱은 일반적인 행렬의 곱 연산과 같음
    
    for d in range(2, n):
        for i in range(n-d):
            j = i+d                 # i부터 i+d까지의 행렬의 곱 구하기
            for k in range(i, j):   # k: i부터 j까지의 곱을 분할하는 기준
                # i부터 k까지, k부터 j까지 이미 연산이 되어 있다는 가정
                # (5, 3), (3, 2), (2, 6)에서 (5, 3) x (3, 2)이 이미 연산되어 있다면, 다음 연산은 (5 x 2 x 6)
                # == matrix[i][0] * matrix[k][1] * matrix[j][1]
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1])

    print(dp[0][n-1])


if __name__ == "__main__":
    main()