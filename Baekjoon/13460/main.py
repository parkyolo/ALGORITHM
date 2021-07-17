from collections import deque

n, m = map(int,input().split())
board = [list(input()) for _ in range(n)]

# 빨간 구슬, 파란 구슬, 구멍의 위치 저장
Rx = Ry = Bx = By = Ox = Oy = -1
for i, col in enumerate(board):
    if 'R' in col:
        Rx = i
        Ry = col.index('R')
    if 'B' in col:
        Bx = i
        By = col.index('B')
    if 'O' in col:
        Ox = i
        Oy = col.index('O')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 아래 위 오른쪽 왼쪽

queue = deque()
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
queue.append([Rx, Ry, Bx, By, 1])
visited[Rx][Ry][Bx][By] = True

def bfs():
    while queue:
        Rx, Ry, Bx, By, cnt = queue.popleft()

        # 10번 이하로 움직여서 빨간 구슬을 빼낼 수 없을 때
        if cnt > 10:
            print(-1)
            return
        
        # 4방향으로 기울이기
        for m in range(4):
            rx = Rx
            ry = Ry
            bx = Bx
            by = By
            cnt_r = cnt_b = 0

            # 구슬 기울이기
            while board[rx+dx[m]][ry+dy[m]] != '#' and board[rx][ry] != 'O':
                cnt_r += 1
                rx += dx[m]
                ry += dy[m]
            while board[bx+dx[m]][by+dy[m]] != '#' and board[bx][by] != 'O':
                cnt_b += 1
                bx += dx[m]
                by += dy[m]

            # 파란 구슬이 구멍에 빠지면 안됨
            if bx == Ox and by == Oy:
                continue

            # 빨간 구슬이 구멍에 빠지면 성공
            if rx == Ox and ry == Oy:
                print(cnt)
                return

            # 두 구슬이 붙어있을 때
            if bx == rx and by == ry:
                if cnt_b > cnt_r:
                    bx -= dx[m]
                    by -= dy[m]
                else:
                    rx -= dx[m]
                    ry -= dy[m]

            # 아직 방문하지 않은 위치일 때만 queue에 넣음
            if not visited[rx][ry][bx][by]:
                queue.append([rx, ry, bx, by, cnt+1])
                visited[rx][ry][bx][by] = True

    # 구멍을 통해 빼낼 수 없을 때
    print(-1)

bfs()