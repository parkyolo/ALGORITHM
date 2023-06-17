from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T = int(input())

def bfs(y, x):
    queue = deque([(y, x)])
    grid[y][x] = '.'
    while queue:
        cy, cx = queue.popleft()
        for d in range(4):
            ny, nx = cy + dxy[d][0], cx + dxy[d][1]
            if ny < 0 or ny >= h or nx < 0 or nx >= w: continue # 범위 체크
            if grid[ny][nx] == '.': continue                    # 방문 체크
            queue.append((ny, nx))
            grid[ny][nx] = '.'

    
for _ in range(T):
    h, w = map(int, input().split())
    grid = list(list(input()) for _ in range(h))
    
    cnt = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                cnt += 1
                bfs(y, x)

    print(cnt)