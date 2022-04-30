N = int(input())
origin_state = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rx = [[0, N, 1], [N-1,-1, -1], [0, N, 1], [0, N, 1]] # rx[i]는 이동방향이 i일 때 x의 범위
ry = [[0, N, 1], [0, N, 1], [0, N, 1], [N-1, -1, -1]] # ry[i]는 이동방향이 i일 때 y의 범위
max_block = max([max(line) for line in origin_state])

def remove_blank(i, j, d, board): # 공백 없애기
    mi, mj = i + dx[d], j + dy[d]
    while 0 <= mi < N and 0 <= mj < N:
        if not board[mi][mj]: # 공백이 있으면 이동
            mi += dx[d]
            mj += dy[d]
        else:
            break
    mi -= dx[d]
    mj -= dy[d]
    if mi != i or mj != j:
        board[mi][mj] = board[i][j]
        board[i][j] = 0

def dfs(board, cnt):
    global max_block
    if cnt == 5: return
    for d in range(4):
        new_board = [[r for r in c] for c in board]
        for i in range(rx[d][0], rx[d][1], rx[d][2]):
            for j in range(ry[d][0], ry[d][1], ry[d][2]):
                # 이동방향에 공백이 있다면 이동
                remove_blank(i, j, d, new_board)
        for i in range(rx[d][0], rx[d][1], rx[d][2]):
            for j in range(ry[d][0], ry[d][1], ry[d][2]):
                # 첫 번째 값(위로 이동한다면 가장 위의 값)부터 다음 값과 같으면 합치기
                if (d == 0 and 0 <= i < N-1) or (d == 1 and 0 < i <= N-1) or (d == 2 and 0 <= j < N-1) or (d == 3 and 0 < j <= N-1): # 마지막 값의 다음 값은 없기 때문에 제외
                    if new_board[i][j] == new_board[i-dx[d]][j-dy[d]]:
                        new_board[i][j] *= 2
                        new_board[i-dx[d]][j-dy[d]] = 0
                        max_block = max(max_block, new_board[i][j])
                # 이동방향에 공백이 있다면 이동
                remove_blank(i, j, d, new_board)
        if board == new_board: continue
        dfs(new_board, cnt+1)

dfs(origin_state, 0)
print(max_block)