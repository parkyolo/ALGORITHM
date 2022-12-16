n = 9
board = list(list(map(int, input().split())) for _ in range(n))

stateRow = [[1 for _ in range(n+1)] for _ in range(n)] # stateRow[i][j]: i번째 행에 j라는 숫자가 있으면 0, 없으면 1
stateCol = [[1 for _ in range(n+1)] for _ in range(n)] # stateCol[i][j]: i번째 열에 j라는 숫자가 있으면 0, 없으면 1
stateArea = [[1 for _ in range(n+1)] for _ in range(n)] # stateArea[i][j]: i번째 영역에 j라는 숫자가 있으면 0, 없으면 1

blank = [] # 비어있는 위치
for i in range(n):
    for j in range(n):
        num = board[i][j]
        if num:
            stateRow[i][num] = 0
            stateCol[j][num] = 0
            stateArea[3*(i//3)+(j//3)][num] = 0 # 왼쪽 위는 0, 오른쪽 아래는 9
        else:
            blank.append((i, j))

def recur(idx):
    if idx == len(blank): # 모든 빈 칸이 다 채워졌으면 출력
        for line in board:
            print(' '.join([str(l) for l in line]))
        exit()

    i, j = blank[idx]
    for ele in range(1, n+1):
        if stateRow[i][ele] and stateCol[j][ele] and stateArea[3*(i//3)+(j//3)][ele]: # 행, 열, 영역에 ele라는 요소가 비어있어야 함
            stateRow[i][ele], stateCol[j][ele], stateArea[3*(i//3)+(j//3)][ele] = 0, 0, 0
            board[i][j] = ele
            recur(idx+1)
            stateRow[i][ele], stateCol[j][ele], stateArea[3*(i//3)+(j//3)][ele] = 1, 1, 1
            board[i][j] = 0    

recur(0)