from collections import deque

n = int(input())
color = list(list(input()) for _ in range(n))
maxCnt = 0

dxyCol = [[-1, 0], [1, 0]]
dxyRow = [[0, -1], [0, 1]]

def getLCA(j, i):   # 가장 긴 연속 부분을 찾는 함수
    global maxCnt
    
    # 행의 연속 부분 길이 구하기
    queue = deque([(j, i)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[j][i] = 1
    cnt = 1
    
    while queue:
        y, x = queue.popleft()
        for d in range(2):
            ny, nx = y + dxyCol[d][0], x + dxyCol[d][1]
            if ny < 0 or ny >= n or nx < 0 or nx >= n: continue
            if visited[ny][nx]: continue
            if color[y][x] != color[ny][nx]: continue
            
            queue.append((ny, nx))
            visited[ny][nx] = 1
            cnt += 1
    
    maxCnt = max(maxCnt, cnt)

    # 열의 연속 부분 길이 구하기
    queue.append((j, i))
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for d in range(2):
            ny, nx = y + dxyRow[d][0], x + dxyRow[d][1]
            if ny < 0 or ny >= n or nx < 0 or nx >= n: continue
            if visited[ny][nx]: continue
            if color[y][x] != color[ny][nx]: continue
            
            queue.append((ny, nx))
            visited[ny][nx] = 1
            cnt += 1
            
    maxCnt = max(maxCnt, cnt)
    
    
for j in range(n):
    for i in range(n):
        # swap하기 전 최대 개수
        getLCA(j, i)
        
        # 행 swap
        if i + 1 < n and color[j][i] != color[j][i+1]:
            color[j][i], color[j][i+1] = color[j][i+1], color[j][i]
            getLCA(j, i)
            getLCA(j, i+1)
            color[j][i], color[j][i+1] = color[j][i+1], color[j][i]
        
        # 열 swap
        if j + 1 < n and color[j][i] != color[j+1][i]:
            color[j][i], color[j+1][i] = color[j+1][i], color[j][i]
            getLCA(j, i)
            getLCA(j+1, i)
            color[j][i], color[j+1][i] = color[j+1][i], color[j][i]

print(maxCnt)