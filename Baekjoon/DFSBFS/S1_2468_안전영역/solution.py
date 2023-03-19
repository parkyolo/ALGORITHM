from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_height = max(max(line) for line in board)
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

max_cnt = 1
for height in range(1, max_height):
    new_board = [[ele for ele in line] for line in board]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if new_board[i][j] == 0 or new_board[i][j] <= height: continue
            cnt += 1
            queue = deque([(i, j)])
            new_board[i][j] = 0
            while queue:
                cx, cy = queue.popleft()
                for d in range(4):
                    nx, ny = cx + dxy[d][0], cy + dxy[d][1]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                    if new_board[nx][ny] == 0 or new_board[nx][ny] <= height: continue
                    queue.append((nx, ny))
                    new_board[nx][ny] = 0
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)