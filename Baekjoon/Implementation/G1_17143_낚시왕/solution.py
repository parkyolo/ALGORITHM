R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
shark_info = {}
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = z
    shark_info[z] = [r-1, c-1, s, d-1] # 같은 크기를 갖는 상어는 없으므로 상어의 크기를 key로 사용

dxy = [[-1, 0], [1, 0], [0, 1], [0, -1]]
change_dir = [1, 0, 3, 2]
caught_shark = 0

# 상어의 다음 위치를 구하는 함수
# loc : 행 또는 열의 위치, length : 행 또는 열의 전체 길이, s : 상어의 속도, d : 상어의 방향, flag : 행을 이동할 때 0 / 열를 이동할 때 1
def get_next_loc(loc, length, s, d, flag): 
    s += loc*dxy[d][flag]               # 1. loc을 0으로 설정하기 위해 상어의 속도에 0과 loc의 차이만큼을 더해줌
    d = 1 if d == 0 or d == 1 else 2    # 2. 방향은 무조건 아래 혹은 오른쪽
    s %= length*2-2                     # 3. 상어가 n 바퀴를 돌아 0으로 다시 돌아왔다고 가정했을 때 남는 거리 계산
    if s >= length:                     # 4. 남은 거리가 전체 행/열의 길이보다 길때
        d = change_dir[d]               #    방향 전환
        s -= (length-1)                 #    행/열의 끝으로 이동
        loc = length - s -1             #    행/열의 끝에서 남은 s만큼 이동
    else:                               # 5. 남은 거리가 전체 행/열의 길이보다 짧을 때
        loc = s                         #    그 길이가 상어의 위치가 됨
    return loc, d                       # 6. 바뀐 위치와 방향 반환

# 상어가 이동하는 함수
def move_shark(): 
    new_board = [[0 for _ in range(C)] for _ in range(R)] # 새로운 격자판
    for row in range(R):
        for col in range(C):
            if board[row][col]:                                         # 1. 상어가 있는 위치
                key = board[row][col] # 상어의 크기
                r, c, s, d = shark_info[key] # 행, 열, 속도, 방향
                if d == 0 or d == 1: r, d = get_next_loc(r, R, s, d, 0) # 2. 다음 위치와 방향을 구함
                else: c, d = get_next_loc(c, C, s, d, 1) 
                        
                shark_info[key] = [r, c, s, d]                          # 3. 정보 갱신
                new_board[r][c] = max(new_board[r][c], key)             # 4. 한 칸에 상어가 두 마리 이상이면 크기가 가장 큰 상어만 남음

    return new_board

# 땅과 제일 가까운 상어를 잡는 함수
def get_shark(col): # col : 낚시왕이 서있는 열 번호
    shark = 0
    for row in range(R): # 땅과 가장 가까운 (행 번호가 가장 작은) 상어를 잡는다.
        if board[row][col]:
            shark = board[row][col]
            board[row][col] = 0 # 잡은 상어 표시
            break
    return shark

for col in range(C):                # 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
    caught_shark += get_shark(col)  # 2. 땅과 가장 가까운 상어를 잡는다.
    board = move_shark()            # 3. 상어가 이동한다.

print(caught_shark)