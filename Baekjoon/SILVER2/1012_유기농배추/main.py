from collections import deque

t = int(input())
for _ in range(t):
    m, n , k = map(int, input().split())
    land = [[0 for _ in range(m)] for _ in range(n)]
    v = [[0 for _ in range(m)] for _ in range(n)] # 방문 확인

    for _ in range(k):
        i, j = map(int, input().split())
        land[j][i] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and v[i][j] == 0: # 아직 방문하지 않은 위치에 배추가 있을 때
                queue = deque()
                queue.append([i,j])
                while queue:
                    x, y = queue.popleft()
                    for d in range(4): # 상하좌우에 인접한 배추가 있는지 탐색
                        if 0 <= x + dx[d] < n and 0 <= y + dy[d] < m:
                            if land[x + dx[d]][y + dy[d]] == 1 and v[x + dx[d]][y + dy[d]] == 0:
                                queue.append([x + dx[d], y + dy[d]])
                                v[x + dx[d]][y + dy[d]] = 1 # 방문 체크
                answer += 1
    print(answer)