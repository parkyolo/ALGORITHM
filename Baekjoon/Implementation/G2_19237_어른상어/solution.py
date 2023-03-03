n, m, k = map(int, input().split())
dxy = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]

shark = {}   # 상어의 위치, 방향

for i in range(n):
    grid = list(map(int, input().split()))
    for j in range(n):
        if grid[j] > 0:
            shark[grid[j]] = [i, j]

direc = list(map(int, input().split()))
for i, d in enumerate(direc):
    shark[i+1].append(d)
    
direc_priority = {}
for i in range(1, m+1):
    direc_priority[i] = [[]]
    for _ in range(4):
        direc_priority[i].append(list(map(int, input().split())))
        
board = [[[0, 0] for _ in range(n)] for _ in range(n)]

def spray_smell():  # 냄새 뿌리기
    for i in range(1, m+1):
        if i not in shark: continue
        x, y, dir = shark[i]
        board[x][y] = [k, i]

def move(): # 상어 이동
    loc = {}    # 상어가 이동할 위치
    for i in range(1, m+1):
        if i not in shark: continue
        x, y, dir = shark[i]
        
        mysmell = []    # 자신의 냄새가 있는 위치
        moved = False   # 이동했는지 검사
        
        for d in direc_priority[i][dir]:
            nx, ny = x + dxy[d][0], y + dxy[d][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if board[nx][ny][0] > 0 and board[nx][ny][1] != i: continue
            
            if board[nx][ny][0] > 0:    # 자신의 냄새가 있는 위치일 때
                mysmell.append(d)
                continue
                
            shark[i] = [nx, ny, d]
            
            if (nx, ny) in loc:                     # 칸에 다른 상어가 있는 경우
                del shark[max(i, loc[(nx, ny)])]    # 번호가 더 큰 상어가 쫓겨남
                loc[(nx, ny)] = min(loc[(nx, ny)], i)
            else:
                loc[(nx, ny)] = i
            
            if loc[(nx, ny)] == i:
                moved = True
                
            break
        
        if not moved and i in shark:    # 이동할 방향이 없는 경우
            d = mysmell[0]              # 자신의 냄새가 있는 칸으로 이동
            nx, ny = x + dxy[d][0], y + dxy[d][1]
            loc[(nx, ny)] = i
            shark[i] = [nx, ny, d]
            
    for i in range(n):  # 기존의 냄새 감소
        for j in range(n):
            if 0 < board[i][j][0] <= k:
                board[i][j][0] -= 1

sec = 0
while len(shark) > 1 and sec <= 1000:
    spray_smell()
    move()
    sec += 1
    
if sec > 1000: print(-1)    # 1000초가 넘으면 -1 출력
else: print(sec)