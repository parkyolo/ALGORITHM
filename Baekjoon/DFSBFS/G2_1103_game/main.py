N, M = 0, 0
max_cnt = 0
board, dp, visited = [], [], []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, cnt):
    global N, M, max_cnt, dp, visited

    max_cnt = max(max_cnt, cnt)
    X = int(board[r][c])
    
    for d in range(4):
        nr, nc = r+dr[d]*X, c+dc[d]*X
        if nr < 0 or nr >= N or nc < 0 or nc >= M or board[nr][nc] == "H" or cnt+1 <= dp[nr][nc]: continue # (nr, nc)를 현재보다 큰 횟수로 방문했다면 continue
        if visited[nr][nc]: # 방문한 곳을 한 번 더 방문했을 때, 게임을 무한으로 즐길 수 있음
            print(-1)
            exit()
        dp[nr][nc] = cnt+1
        visited[nr][nc] = True
        dfs(nr, nc, cnt+1)
        visited[nr][nc] = False

def main():
    global N, M, board, dp, visited
    N, M = map(int, input().split())
    board = list(list(input()) for _ in range(N)) # 게임판
    dp = [[0 for _ in range(M)] for _ in range(N)] # 해당 위치까지 움직인 최대 횟수
    visited = [[False for _ in range(M)] for _ in range(N)] # 방문 여부
    
    dfs(0, 0, 1)
                
    print(max_cnt)                

if __name__ == "__main__":
    main()