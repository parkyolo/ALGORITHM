from collections import deque

t = int(input())
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    answer = 0
    for y in range(n):
        for x in range(m):
            if board[y][x]: # 아직 방문하지 않은 위치에 배추가 있을 때
                answer += 1
                queue = deque([(y, x)])
                board[y][x] = 0
                
                while queue:
                    cy, cx = queue.popleft()
                    for d in range(4): # 상하좌우에 인접한 배추가 있는지 탐색
                        ny, nx = cy + dxy[d][0], cx + dxy[d][1]
                        if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
                        if not board[ny][nx]: continue
                        queue.append((ny, nx))
                        board[ny][nx] = 0
                
    print(answer)