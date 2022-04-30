from collections import deque

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 5 # 사과의 위치

L = int(input())
dir_trans_info = deque() # 뱀의 방향 변환 정보
for _ in range(L):
    x, c = input().split()
    dir_trans_info.append([int(x), c])

# 0:상, 1:하, 2:좌, 3:우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
trans_dir = {'L':[2, 3, 1, 0], 'D':[3, 2, 0, 1]} # 왼쪽 또는 오른쪽으로 90도 회전시켰을 때의 방향
snake_dir = 3 # 뱀은 처음에 오른쪽을 향한다.
snake = deque([(0, 0)])
sec = 0

ns, nd = dir_trans_info.popleft() # 뱀의 방향이 변하는 시간과 회전 방향
while True:
    sec += 1
    hx, hy = snake[-1] # 뱀의 머리
    nx, ny = hx+dx[snake_dir], hy+dy[snake_dir] # 다음 칸

    if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in snake: break # 뱀이 벽 또는 자기자신의 몸과 부딪히면 게임 끝
    snake.append((nx, ny)) # 머리를 다음칸에 위치시킴
    
    if board[nx][ny] == 5: # 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
        board[nx][ny] = 0
    else: # 사과가 없다면, 꼬리를 pop
        snake.popleft()    

    if sec == ns: # 게임 시작 시간으로부터 X초가 끝난 후
        snake_dir = trans_dir[nd][snake_dir]
        if dir_trans_info:
            ns, nd = dir_trans_info.popleft()
        
print(sec)