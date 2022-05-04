dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def Aturn(board, ax, ay, bx, by, cnt):

    if board[ax][ay] == 0: # 서있던 발판이 사라진 경우
        return 0, cnt

    win = []
    lose = []

    can_move = False # 움직일 곳이 있는지 확인
    for i in range(4):
        nax, nay = ax+dx[i], ay+dy[i]
        if nax < 0 or nax >= len(board) or nay < 0 or nay >= len(board[0]) or not board[nax][nay]: continue
        can_move = True
        new_board = [[c for c in r] for r in board]
        new_board[ax][ay] = 0
        iswin, move_cnt = Bturn(new_board, nax, nay, bx, by, cnt+1) # B의 승패 여부와 이동 횟수
        if iswin: # 상대가 이기면 나는 진다.
            lose.append(move_cnt)
        else:
            win.append(move_cnt)
    
    if can_move:
        if win: # 이길 수 있는 방법이 있을 때
            return 1, min(win)
        else: # 무조건 질 수밖에 없을 때
            return 0, max(lose)
    else: # 상하좌우 4칸이 모두 발판이 없거나 보드 밖일 때
        return 0, cnt

def Bturn(board, ax, ay, bx, by, cnt):

    if board[bx][by] == 0: # 서있던 발판이 사라진 경우
        return 0, cnt

    win = []
    lose = []

    can_move = False # 움직일 곳이 있는지 확인
    for i in range(4):
        nbx, nby = bx+dx[i], by+dy[i]
        if nbx < 0 or nbx >= len(board) or nby < 0 or nby >= len(board[0]) or not board[nbx][nby]: continue
        can_move = True
        new_board = [[c for c in r] for r in board]
        new_board[bx][by] = 0
        iswin, move_cnt = Aturn(new_board, ax, ay, nbx, nby, cnt+1) # A의 승패 여부와 이동 횟수
        if iswin: # 상대가 이기면 나는 진다.
            lose.append(move_cnt)
        else:
            win.append(move_cnt)
    
    if can_move:
        if win: # 이길 수 있는 방법이 있을 때
            return 1, min(win)
        else: # 무조건 질 수밖에 없을 때
            return 0, max(lose)
    else: # 상하좌우 4칸이 모두 발판이 없거나 보드 밖일 때
        return 0, cnt
    
def solution(board, aloc, bloc):
    _, cnt = Aturn(board, aloc[0], aloc[1], bloc[0], bloc[1], 0) # A가 먼저 시작
    return cnt

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]), 5)
print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]), 4)
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]), 4)