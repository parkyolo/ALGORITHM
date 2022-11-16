n, board = 0, []
dp = []
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def get_dist(x, y):
    dp[x][y] = 1    # 초기화

    for i in range(4):
        nx, ny = x + dxy[i][0], y + dxy[i][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if board[nx][ny] > board[x][y]:

            if not dp[nx][ny]:
                get_dist(nx, ny)

            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)

    return dp[x][y]


def main():
    global n, board, dp

    n = int(input())
    board = list(list(map(int, input().split())) for _ in range(n))

    dp = [[0 for _ in range(n)] for _ in range(n)] # dp[x][y]: (x, y)에서 출발했을 때 최대 이동 거리

    answer = 0

    for x in range(n):
        for y in range(n):
            if not dp[x][y]:
                get_dist(x, y)
                answer = max(answer, dp[x][y])
    
    print(answer)


if __name__ == "__main__":
    main()