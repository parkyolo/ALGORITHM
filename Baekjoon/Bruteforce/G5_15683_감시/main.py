from itertools import product
from copy import deepcopy
from collections import deque
import sys

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]

direcs = [] # cctv 방향의 경우의 수
for i in range(n):
    for j in range(m):
        if office[i][j] == 1 or office[i][j] == 3 or office[i][j] == 4:
            direcs.append([(i,j,0),(i,j,1),(i,j,2),(i,j,3)])
        elif office[i][j] == 2:
            direcs.append([(i,j,0),(i,j,1)])
        elif office[i][j] == 5:
            direcs.append([(i,j,0)])
combi = list(product(*direcs))

if not direcs: # cctv가 없을 경우
    print(sum([off.count(0) for off in office]))
    exit()

direc = [[0,1],[1,0],[0,-1],[-1,0]]
queue = deque()
result = sys.maxsize
for c in combi:
    _map = deepcopy(office)
    for i,j,d in c:
        if _map[i][j] == 1:
            queue.append([i,j])
            while queue:
                x, y = queue.popleft()
                if 0 <= x+direc[d][0] < n and 0 <= y+direc[d][1] < m:
                    if _map[x+direc[d][0]][y+direc[d][1]] != 6:
                        if _map[x+direc[d][0]][y+direc[d][1]] == 0:
                            _map[x+direc[d][0]][y+direc[d][1]] = '#'
                        queue.append([x+direc[d][0], y+direc[d][1]])
        elif _map[i][j] == 2:
            for k in range(2):
                queue.append([i,j])
                while queue:
                    x, y = queue.popleft()
                    if 0 <= x+direc[d+k*2][0] < n and 0 <= y+direc[d+k*2][1] < m:
                        if _map[x+direc[d+k*2][0]][y+direc[d+k*2][1]] != 6:
                            if _map[x+direc[d+k*2][0]][y+direc[d+k*2][1]] == 0:
                                _map[x+direc[d+k*2][0]][y+direc[d+k*2][1]] = '#'
                            queue.append([x+direc[d+k*2][0], y+direc[d+k*2][1]])
        elif _map[i][j] == 3:
            for k in range(2):
                queue.append([i,j])
                while queue:
                    x, y = queue.popleft()
                    if 0 <= x+direc[(4+d-k)%4][0] < n and 0 <= y+direc[(4+d-k)%4][1] < m:
                        if _map[x+direc[(4+d-k)%4][0]][y+direc[(4+d-k)%4][1]] != 6:
                            if _map[x+direc[(4+d-k)%4][0]][y+direc[(4+d-k)%4][1]] == 0:
                                _map[x+direc[(4+d-k)%4][0]][y+direc[(4+d-k)%4][1]] = '#'
                            queue.append([x+direc[(4+d-k)%4][0], y+direc[(4+d-k)%4][1]])
        elif _map[i][j] == 4:
            w = [2,3,0,1]
            for k in range(3):
                queue.append([i,j])
                while queue:
                    x, y = queue.popleft()
                    di = w[(d+k)%4]
                    if 0 <= x+direc[di][0] < n and 0 <= y+direc[di][1] < m:
                        if _map[x+direc[di][0]][y+direc[di][1]] != 6:
                            if _map[x+direc[di][0]][y+direc[di][1]] == 0:
                                _map[x+direc[di][0]][y+direc[di][1]] = '#'
                            queue.append([x+direc[di][0], y+direc[di][1]])
        elif _map[i][j] == 5:
            for k in range(4):
                queue.append([i,j])
                while queue:
                    x, y = queue.popleft()
                    if 0 <= x+direc[k][0] < n and 0 <= y+direc[k][1] < m:
                        if _map[x+direc[k][0]][y+direc[k][1]] != 6:
                            if _map[x+direc[k][0]][y+direc[k][1]] == 0:
                                _map[x+direc[k][0]][y+direc[k][1]] = '#'
                            queue.append([x+direc[k][0], y+direc[k][1]])

        cnt = sum([m.count(0) for m in _map])
        result = min(result, cnt)
print(result)