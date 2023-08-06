'''
1949. [모의 SW 역량테스트] 등산로 조성
(https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE&problemTitle=1949&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

시작 점을 찾고, DFS로 가장 긴 거리를 찾음
'''

T = int(input())
n, k = 0, 0
map_ = []

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
max_length = 0

# 최장 거리를 갱신하고 다음 4방향으로 이동할 수 있는지 확인하는 함수
def dfs(r, c, cnt, height, flag): # 좌표 r, c, 이동 거리, 현재 지형의 높이, 공사 여부
    global max_length
    max_length = max(max_length, cnt)   # 최장 거리 갱신

    for d in range(4):
        nr, nc = r+dxy[d][0], c+dxy[d][1]
        if nr < 0 or nr >= n or nc < 0 or nc >= n: continue # 범위 안에 들어오는지 확인
        if map_[nr][nc] == -1: continue                     # 방문 확인
        if map_[nr][nc] < height:                           # 1. 높이가 더 낮으면 이동
            nh = map_[nr][nc]
            map_[nr][nc] = -1
            dfs(nr, nc, cnt+1, nh, flag)
            map_[nr][nc] = nh
        elif flag: continue                                 # 2. 높이가 더 낮지 않고 이미 지형을 깎았으면 넘어감
        elif map_[nr][nc] - height < k:                     # 3. 지형을 깎아서 이동할 수 있다면 이동
            nh = map_[nr][nc]
            map_[nr][nc] = -1
            dfs(nr, nc, cnt+1, height-1, True)
            map_[nr][nc] = nh

# 시작 점에 방문을 체크하고 dfs를 시작하는 함수
def construction(start_point):
    for r, c in start_point:
        height = map_[r][c]
        map_[r][c] = -1
        dfs(r, c, 1, height, False)
        map_[r][c] = height

# 가장 높은 지형(시작 점)을 찾아서 넘겨주는 함수
def solution():
    global n, k, map_, max_length
    n, k = map(int, input().split())
    map_ = list(list(map(int, input().split())) for _ in range(n))
    max_length = 0

    start_point = []
    max_height = max([max(line) for line in map_]) # 가장 높은 지형의 높이
    for r in range(n):
        for c in range(n):
            if map_[r][c] == max_height:
                start_point.append([r, c])
    
    construction(start_point) # 공사 시작

for test_case in range(1, T + 1):
    solution()
    print("#%d %d"%(test_case, max_length))