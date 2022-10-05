r, c, t, board = 0, 0, 0, []
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def spreading(): # 미세먼지 확산

    spread = [[0 for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                temp = 0
                for k in range(4):                                                              # 1. (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
                    nx, ny = x+dxy[k][0], y+dxy[k][1]
                    if nx < 0 or nx >= r or  ny < 0 or ny >= c or board[nx][ny] == -1: continue # 2. 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                    spread[nx][ny] += board[x][y] // 5                                          # 3. 확산되는 양은 A(r,c)/5이고 소수점은 버린다. 
                    temp += board[x][y] // 5
                board[x][y] -= temp                                                             # 4. (r, c)에 남은 미세먼지의 양은 A(r,c) - (A(r,c)/5) × (확산된 방향의 개수)이다.

    for x in range(r):
        for y in range(c):
            board[x][y] += spread[x][y]

def cleaning(loc, o1, o2): # 공기청정기 작동

    for x in range(loc+o2, o1, o2): # 0열 ↓/↑ 방향 이동
        board[x][0] = board[x+o2][0]
    for y in range(c-1):            # o1행 ← 방향 이동
        board[o1][y] = board[o1][y+1]
    for x in range(o1, loc, -o2):   # c-1열 ↑/↓ 방향 이동
        board[x][c-1] = board[x-o2][c-1]
    for y in range(c-1, 1, -1):     # loc행 → 방향 이동
        board[loc][y] = board[loc][y-1]

    board[loc][1] = 0               # 공기청정기 옆
    

def main():
    global r, c, t, board
    r, c, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]

    air_cleaner = [i for j in range(c) for i in range(r) if board[i][j] == -1] # 공기청정기의 행의 위치 저장

    for _ in range(t):
        spreading()                     # 1. 미세먼지 확산
        cleaning(air_cleaner[0], 0, -1) # 2. 공기청정기 작동
        cleaning(air_cleaner[1], r-1, 1)

    print(sum([sum(line) for line in board])+2)

if __name__ == "__main__":
    main()