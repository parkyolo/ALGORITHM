import sys
n,m,b = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_t = sys.maxsize
min_t_h = -1
for h in range(257):
    higher = 0 # h보다 높은 땅의 개수
    lower = 0 # h보다 낮은 땅의 개수
    for i in range(n):
        for j in range(m):
            if land[i][j] > h: higher += land[i][j] - h
            else: lower += h - land[i][j] # elif로 조건을 주면 시간초과가 남
    
    if higher + b < lower: continue
    t = higher * 2 + lower # 땅을 고르는 데 걸리는 시간
    if t <= min_t:
        min_t = t
        min_t_h = h

print(f"{min_t} {min_t_h}")