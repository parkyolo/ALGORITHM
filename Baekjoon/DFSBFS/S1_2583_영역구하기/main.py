from collections import deque

M, N, K = map(int, input().split())
grid = [[0 for _ in range(N)] for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[j][i] = 1

def bfs(i, j):
    queue = deque([(i,j)])
    grid[i][j] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or nx >= M or ny < 0 or ny >= N or grid[nx][ny]: continue
            grid[nx][ny] = 1
            cnt += 1
            queue.append((nx, ny))
    return cnt

for i in range(M):
    for j in range(N):
        if not grid[i][j]:
            answer.append(bfs(i, j))
            
answer.sort()
print(len(answer))
for a in answer:
    print(a, end=' ')