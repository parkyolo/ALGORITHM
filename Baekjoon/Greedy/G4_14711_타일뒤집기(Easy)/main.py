N = int(input())
board = [list(input())]+[["" for _ in range(N)] for _ in range(N-1)] # 게임판의 상태

# 상하좌우 변화량
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = [[0 for _ in range(N)] for _ in range(N)] # 타일이 뒤집히는 횟수
for i in range(N):
    if board[0][i] == '#': # 타일이 #이면
        cnt[0][i] += 1 # 해당 타일과
        for d in range(4): # 상하좌우로 인접한 타일이 뒤집힘
            nx, ny = dx[d], i+dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            cnt[nx][ny] += 1

# #은 뒤집는 횟수가 홀수, .은 뒤집는 횟수가 짝수여야 함
for i in range(N-1):
    for j in range(N):
        if (board[i][j] == '.' and cnt[i][j] % 2 == 0) or (board[i][j] == '#' and cnt[i][j] % 2 == 1): # 타일이 알맞는 횟수로 뒤집히면
            board[i+1][j] = '.' # 아래 타일은 뒤집힐 필요 없으므로 .
            continue
        board[i+1][j] = '#' # 뒤집는 횟수가 알맞지 않으면 한 번 더 뒤집어야 하므로 아래에 # 타일을 놓음
        cx, cy = i+1, j
        cnt[cx][cy] += 1 # 해당 타일과 인접한 타일의 뒤집히는 횟수 +=1
        for d in range(4):
            nx, ny = cx+dx[d], cy+dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            cnt[nx][ny] += 1

for line in board:
    print(''.join(line))