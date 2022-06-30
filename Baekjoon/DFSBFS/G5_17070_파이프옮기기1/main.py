N, board = 0, []
answer = 0

def dfs(x, y, d): # d = 가로 0, 세로 1, 대각선 2
    global answer

    if x == N-1 and y == N-1:
        answer += 1
        return

    if d == 0 or d == 2: # 가로로 이동할 수 있는 경우
        if y + 1 < N and not board[x][y+1]:
            dfs(x, y+1, 0)
    
    if d == 1 or d == 2: # 세로로 이동할 수 있는 경우
        if x + 1 < N and not board[x+1][y]:
            dfs(x+1, y, 1)
    
    # 대각선은 모든 방향에서 이동할 수 있음
    if x + 1 < N and y + 1 < N and not board[x][y+1] and not board[x+1][y] and not board[x+1][y+1]:
        dfs(x+1, y+1, 2)


def main():
    global N, board
    N = int(input())
    board = list(list(map(int, input().split())) for _ in range(N))

    dfs(0, 1, 0)
    print(answer)

if __name__ == "__main__":
    main()