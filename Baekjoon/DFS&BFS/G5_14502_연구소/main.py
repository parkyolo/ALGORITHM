from itertools import combinations
from copy import deepcopy
from collections import deque

n, m = map(int, input().split())
lap = [list(map(int, input().split())) for _ in range(n)] # 연구소

zero_area = [] # 빈 칸 위치
virus_area = [] # 바이러스 위치
for i in range(n):
    for j in range(m):
        if lap[i][j] == 0: zero_area.append((i, j))
        elif lap[i][j] == 2: virus_area.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safe_area = 0 # 안전 영역의 크기
combi = list(combinations(zero_area, 3)) # 빈 칸 중 벽을 세울 곳 3개를 뽑음
for t in combi:
    new_lap = deepcopy(lap)
    infected = 0 # 바이러스가 퍼진 영역의 크기

    for i, j in t: # 벽 세우기
        new_lap[i][j] = 1

    queue = deque(virus_area)
    while queue: # 바이러스 퍼트리기
        x, y = queue.popleft()
        for d in range(4): 
            if 0 <= x+dx[d] < n and 0 <= y+dy[d] < m:
                if new_lap[x+dx[d]][y+dy[d]] == 0:
                    new_lap[x+dx[d]][y+dy[d]] = 2
                    queue.append((x+dx[d], y+dy[d]))
                    infected += 1
    
    safe_area = max(safe_area, len(zero_area) - infected - 3)

print(safe_area)