def solution(grid):
    answer = []

    # 빛이 오는 방향에 따른 이동 방향
    # [상, 하, 좌, 우]
    dx = [[1, -1, 0, 0], [0, 0, -1, 1], [0, 0, 1, -1]]
    dy = [[0, 0, 1, -1], [1, -1, 0, 0], [-1, 1, 0, 0]]

    # 직전 방향이 S, L, R일 때 빛이 온 방향
    # 상 : 0, 하 : 1, 좌 : 2, 우 : 3
    dz = [[0, 1, 2, 3], [2, 3, 1, 0], [3, 2, 0, 1]]
    
    # 방향 방문 여부를 포함한 matrix 생성
    m = len(grid[0])*2 # matrix의 가로 길이
    n = len(grid)*2 # matrix의 세로 길이
    matrix = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i%2 == 0 and j%2 == 0: continue
            matrix[i][j] = [0, 0]

    points = [] # 격자의 모든칸을 저장
    for i, g in enumerate(grid):
        for j, c in enumerate(g):
            matrix[2*i+1][2*j+1] = c
            points.append([2*i+1, 2*j+1])
    
    for p in points: # 모든 칸을 시작점으로 사이클을 시작
        for start in range(4):
            cnt = 0
            cur_d = start # 현재 빛이 온 방향
            cur_i, cur_j = p[0], p[1] # 현재 grid 좌표
            while True:
                d = -1 # S : 0, L : 1, R : 2
                if matrix[cur_i][cur_j] == 'S':
                    d = 0
                elif matrix[cur_i][cur_j] == 'L':
                    d = 1
                elif matrix[cur_i][cur_j] == 'R':
                    d = 2

                if 0 <= cur_i + dx[d][cur_d] < n and 0 <= cur_j + dy[d][cur_d] < m:
                    cur_i += dx[d][cur_d]
                    cur_j += dy[d][cur_d]
                elif cur_i + dx[d][cur_d] >= n:
                    cur_i = 0
                elif cur_i + dx[d][cur_d] < 0:
                    cur_i = n-1
                elif cur_j + dy[d][cur_d] >= m:
                    cur_j = 0
                elif cur_j + dy[d][cur_d] < 0:
                    cur_j = m-1

                next_d = -1 # 다음으로 빛이 갈 방향
                if dz[d][cur_d] == 0 or dz[d][cur_d] == 2:
                    next_d = 1
                else:
                    next_d = 0
                if matrix[cur_i][cur_j][next_d] == 1:
                    if cnt > 0:
                        answer.append(cnt)
                    break
                else:
                    matrix[cur_i][cur_j][next_d] = 1
                    if 0 <= cur_i + dx[d][cur_d] < n and 0 <= cur_j + dy[d][cur_d] < m:
                        cur_i += dx[d][cur_d]
                        cur_j += dy[d][cur_d]
                    elif cur_i + dx[d][cur_d] < 0:
                        cur_i = n-1
                    elif cur_j + dy[d][cur_d] < 0:
                        cur_j = m-1
                    cnt += 1
                    cur_d = dz[d][cur_d]
    
    answer.sort()
    return answer

print(solution(["SL","LR"]),[16])
print(solution(["S"]),[1,1,1,1])
print(solution(["R","R"]),[4,4])