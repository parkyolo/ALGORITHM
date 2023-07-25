n, k = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n)) # 체스판 상태

horse_info = []     # horse_info[i]: i번째 말의 행, 열의 번호, 이동 방향
horse_coord = {}    # horse_coord[(r, c)]: board의 (r,c)에 있는 말의 index

for i in range(k):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    horse_info.append([r, c, d])
    if (r, c) in horse_coord:
        horse_coord[(r, c)].append(i)
    else:
        horse_coord[(r, c)] = [i]

drc = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]    # 이동 방향 →, ←, ↑, ↓

def move(r, c):
    global flag
    horse_idx = horse_coord[(r, c)][0]  # 현재 움직일 말의 index
    dir = horse_info[horse_idx][2]      # 말의 이동 방향
    nr, nc = r + drc[dir][0], c + drc[dir][1]   # 말의 위치
    
    # 칸이 파란색이거나 말이 체스판을 벗어나는 경우
    if nr < 0 or nr >= n or nc < 0 or nc >= n or board[nr][nc] == 2:    
        dir = dir - 1 if dir % 2 == 0 else dir + 1  # 이동 방향을 반대로 하고
        nr, nc = r + drc[dir][0], c + drc[dir][1]   # 한 칸 이동한다.
        horse_info[horse_idx][2] = dir
        # 방향을 반대로 한 후에 이동하려는 칸이 파란색인 경우
        # 이동하지 않고 방향만 반대로 바꾼다.
        if nr < 0 or nr >= n or nc < 0 or nc >= n or board[nr][nc] == 2:
            return
        
    # (r,c)에 있는 모든 말들 한 칸 이동
    for cur_idx in horse_coord[(r, c)]:
        horse_info[cur_idx][0] = nr
        horse_info[cur_idx][1] = nc

    # 칸이 빨간색인 경우 모든 말의 쌓여있는 순서를 반대로 바꾼다.
    if board[nr][nc] == 1:
        if (nr, nc) in horse_coord:
            horse_coord[(nr, nc)] += list(reversed(horse_coord[(r, c)]))
        else:
            horse_coord[(nr, nc)] = list(reversed(horse_coord[(r, c)]))
    # 칸이 흰색인 경우
    else:
        # 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 이동하는 말들을 올려놓는다.
        if (nr, nc) in horse_coord:
            horse_coord[(nr, nc)] += horse_coord[(r, c)]
        else:
            horse_coord[(nr, nc)] = horse_coord[(r, c)]
    del horse_coord[(r, c)]
    
    # 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.
    if len(horse_coord[(nr, nc)]) >= 4:
        flag = False

def play():
    for i in range(k):
        if not flag:
            return
        mr, mc = horse_info[i][0], horse_info[i][1] # i번째 말의 현재 위치
        if horse_coord[(mr, mc)][0] == i:           # 가장 아래에 있는 말만 이동할 수 있다.
            move(mr, mc)


turn = 0    # turn이 1,000보다 커지면 -1 출력
flag = True # 말이 4개 이상 쌓이면 False
while turn <= 1000 and flag:
    turn += 1
    play()
    
if turn > 1000:
    print(-1)
else:
    print(turn)