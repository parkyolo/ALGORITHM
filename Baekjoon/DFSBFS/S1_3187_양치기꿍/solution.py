from collections import deque

r, c = map(int, input().split())
board = list(list(input()) for _ in range(r))
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

survived_wolves, survived_sheep = 0, 0

def bfs(y, x):
    global survived_wolves, survived_sheep
    
    wolves, sheep = 0, 0
    if board[y][x] == 'v': wolves += 1
    elif board[y][x] == 'k': sheep += 1
    
    queue = deque([(y, x)])
    board[y][x] = '#'   # 방문 체크
    
    while queue:
        cy, cx = queue.popleft()
        for d in range(4):
            ny, nx = cy + dxy[d][0], cx + dxy[d][1]
            if ny < 0 or ny >= r or nx < 0 or nx >= c: continue
            if board[ny][nx] == '#': continue
            
            if board[ny][nx] == 'v': wolves += 1
            elif board[ny][nx] == 'k': sheep += 1
            
            board[ny][nx] = '#'
            queue.append((ny, nx))
    
    if sheep > wolves: survived_sheep += sheep
    else: survived_wolves += wolves

for y in range(r):
    for x in range(c):
        if board[y][x] != '#':
            bfs(y, x)

print(survived_sheep, survived_wolves)