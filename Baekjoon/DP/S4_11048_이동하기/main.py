N, M = map(int, input().split())
board = [[0 for _ in range(M+1)]]+ list([0] + list(map(int, input().split())) for _ in range(N))

for r in range(1, N+1):
    for c in range(1, M+1):
        board[r][c] += max([board[r-1][c], board[r][c-1], board[r-1][c-1]])

print(board[N][M])