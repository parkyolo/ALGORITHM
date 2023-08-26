from collections import deque
n = int(input())
picture = ['-'*(n+2)] + ['-'+input()+'-' for _ in range(n)] + ['-'*(n+2)]
v = [[0 for _ in range(n+2)] for _ in range(n+2)]
c_v = [[0 for _ in range(n+2)] for _ in range(n+2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
c_cnt = 0
queue = deque()
for i in range(1, n+1):
    for j in range(1, n+1):
        if v[i][j] == 0: # 적록색약이 아닌 사람
            v[i][j] = 1
            queue.append((i,j))
            color = picture[i][j]
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    if picture[x+dx[d]][y+dy[d]] == color and v[x+dx[d]][y+dy[d]] == 0:
                        v[x+dx[d]][y+dy[d]] = 1
                        queue.append((x+dx[d], y+dy[d]))
            cnt += 1
        if c_v[i][j] == 0: # 적록색약인 사람
            c_v[i][j] = 1
            queue.append((i,j))
            color = set()
            if picture[i][j] == 'B':
                color.add('B')
            else: color.update(['R', 'G'])
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    if picture[x+dx[d]][y+dy[d]] in color and c_v[x+dx[d]][y+dy[d]] == 0:
                        c_v[x+dx[d]][y+dy[d]] = 1
                        queue.append((x+dx[d], y+dy[d]))
            c_cnt += 1

print(cnt, c_cnt)