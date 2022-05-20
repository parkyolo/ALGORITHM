M, N = map(int, input().split())
map_ = list(list(map(int, input().split())) for _ in range(M))
dp = [[-1 for _ in range(N)] for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(cx, cy):
    if cx == M-1 and cy == N-1:
        return 1

    result = 0 # (cx, cy)에서 출발하는 경로의 개수
    for i in range(4):
        nx, ny = cx+dx[i], cy+dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        if map_[nx][ny] < map_[cx][cy]:
            if dp[nx][ny] > -1: # 이미 탐색했던 경로이면
                result += dp[nx][ny] # 그 경로의 개수를 result에 더해줌
            else: # 처음 가는 경로이면 dfs
                result += dfs(nx, ny)
                
    dp[cx][cy] = result
    return result

result = dfs(0, 0)
print(result)