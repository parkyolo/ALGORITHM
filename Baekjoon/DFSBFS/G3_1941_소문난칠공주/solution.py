N = 7
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

board = list(list(input()) for _ in range(5))

visited = [0 for _ in range(1<<25)] # 경로 방문 체크
cnt = 0

def dfs(path, ss, yy):  # 경로, 이다솜파, 임도연파
    global cnt
    
    if yy >= 4: return
    if ss + yy == N: 
        cnt += 1
        return
    
    for node in range(25):	# 현재 경로에 속한 모든 노드를 검사
        if (not path & (1<<node)): continue
        
        x, y = int(node / 5), int(node % 5)   # 현재 위치
        
        for d in range(4):
            nx, ny = x + dxy[d][0], y + dxy[d][1]   # 인접 위치
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5: continue
            
            num = nx * 5 + ny   # 인접 위치의 번호
            if visited[path|(1<<num)]: continue # 방문한 적 있는 경로인지 체크
            visited[path|(1<<num)] = 1
            
            if board[nx][ny] == 'S':
                dfs(path|(1<<num), ss+1, yy)
            else:
                dfs(path|(1<<num), ss, yy+1)


# 0부터 25개의 자리에서 탐색 시작
for i in range(5):
    for j in range(5):
        num = i * 5 + j
        visited[1<<num] = 1
        if board[i][j] == 'S':
            dfs(1<<num, 1, 0)
        else:
            dfs(1<<num, 0, 1)


print(cnt)