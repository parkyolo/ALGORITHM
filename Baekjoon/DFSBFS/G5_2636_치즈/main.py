from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
remain = [] # 녹인 치즈 개수
time = 0 # 치즈가 녹아서 없어지는 데 걸리는 시간
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while True:
    cnt = 0
    v = [[0 for _ in range(m)] for _ in range(n)] # 방문체크
    queue.append((0, 0))
    v[0][0] = 1 # 가장자리는 공기
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
                if not board[nx][ny]:
                    v[nx][ny] = 1
                    queue.append((nx, ny))
                elif board[nx][ny]: # 공기와 닿아있는 치즈
                    board[nx][ny] = 0
                    v[nx][ny] = 1
                    cnt += 1
    remain.append(cnt)
    time += 1
    if not cnt: break
    
print(time-1)
print(remain[-2])
