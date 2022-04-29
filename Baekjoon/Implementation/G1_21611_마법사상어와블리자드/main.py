N, M = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))
magic = list(list(map(int, input().split())) for _ in range(M))

num_grid = dict() # i:board[r][c]
loc_grid = dict() # (r,c) : i
dx = [0, 1, 0, -1] # ←,↓,→,↑
dy = [-1, 0, 1, 0]
attack_dir = {1:3, 2:1, 3:0, 4:2} # 공격 방향을 dx,dy의 인덱스에 맞게 바꿔줌
ans = [0, 0, 0, 0] # 폭발한 구슬의 개수

def init_grid(): # 초기화
    global N
    x, y = N//2, N//2
    dir, moved, turn = 0, 0, 0 # 방향, 움직인 횟수, 방향을 바꾼 횟수
    move_cnt, idx = 1, 1 # 현재 방향으로 움직여야 하는 횟수, 칸의 번호

    # 시작 위치
    num_grid[0] = 0
    loc_grid[(x, y)] = 0

    while True:
        if x == 0 and y == 0: break # 종료 위치

        x += dx[dir] # 이동
        y += dy[dir]

        num_grid[idx] = board[x][y] # 칸의 번호 : 구슬의 번호
        loc_grid[(x, y)] = idx # 칸의 위치 : 칸의 번호

        idx += 1 # 칸의 번호 += 1
        moved += 1 # 움직인 횟수 += 1

        if moved == move_cnt: # move_cnt번 움직였다면 방향 바꾸기
            dir = (dir+1)%4
            turn += 1
            moved = 0
        if turn == 2: # 2번 방향을 바꿨다면 움직여야하는 횟수 증가
            move_cnt += 1
            turn = 0

def attack(d, s): # d의 방향으로 s만큼 구슬 파괴
    dir = attack_dir[d]
    x, y = N//2, N//2
    for _ in range(s):
        x += dx[dir]
        y += dy[dir]
        loc = loc_grid[(x, y)]
        num_grid[loc] = -1 # 파괴한 구슬을 -1로 표시

def move(): # 구슬 이동
    global num_grid
    new_ng = dict()
    idx = 0
    for i in range(N*N):
        if num_grid[i] == -1: continue
        new_ng[idx] = num_grid[i]
        idx += 1

    num_grid = new_ng
    for i in range(len(new_ng), N*N):
        num_grid[i] = 0

def bomb(): # 구슬 폭발
    global ans
    bombed = []
    check = False
    for i in range(1, N*N):
        if num_grid[i] == num_grid[i-1]:
            bombed.append(i-1)
        if len(bombed) > 0 and num_grid[i] != num_grid[i-1]:
            if len(bombed) >= 3:
                ans[num_grid[i-1]] += len(bombed) + 1
                check = True
                num_grid[i-1] = -1
                for b in bombed:
                    num_grid[b] = -1
            bombed = []
    return check

def change(): # 구슬 변화
    global num_grid
    new_ng = {0:0}
    same = []
    idx = 1
    for i in range(1, N*N-1):
        if num_grid[i] == 0 or idx >= N*N: break
        if num_grid[i] == num_grid[i+1]:
            same.append(i)
        else:
            if len(same) > 0:
                new_ng[idx] = len(same)+1
                new_ng[idx+1] = num_grid[i]
                idx += 2
                same = []
            else:
                new_ng[idx] = 1
                new_ng[idx+1] = num_grid[i]
                idx += 2
    num_grid = new_ng
    for i in range(len(new_ng), N*N):
        num_grid[i] = 0

init_grid()
for d, s in magic:
    attack(d, s)
    move()
    while True:
        if not bomb(): break
        move()
    change()

print(ans[1]+2*ans[2]+3*ans[3])