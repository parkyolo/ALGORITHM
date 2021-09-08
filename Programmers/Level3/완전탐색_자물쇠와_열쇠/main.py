def turn(key,m): # key를 90도 회전
    rotated = []
    for i in range(m):
        temp = []
        for j in range(m-1,-1,-1):
            temp.append(key[j][i])
        rotated.append(temp)
    return rotated

def makeboard(m,n,lock): # 가운데에 lock이 있는 (2(m-1)+n)x(2(m-1)+n) 모양 보드 생성
    board = [[0 for _ in range(2*m+n-2)] for _ in range(2*m+n-2)]
    li = lj = 0
    for i in range(m-1, m+n-1):
        for j in range(m-1, m+n-1):
            board[i][j] = lock[li][lj]
            lj += 1
        li += 1
        lj = 0
    return board

def try_open(i,j,m,n,key,lock): # 보드에 key 값을 더함
    # 새로운 보드 생성
    board = makeboard(m,n,lock)
    # 보드에서 key의 범위만큼 더해줌
    for s in range(i,i+m):
        for e in range(j,j+m):
            board[s][e] = board[s][e] + key[s-i][e-j]
    return board

def unlock(board, m, n):
    check = True
    # lock의 범위만큼 모든 값이 1인지 검사
    # 모든 값이 1이면 자물쇠를 열 수 있음
    for i in range(m-1, m+n-1):
        if check == False: break
        for j in range(m-1, m+n-1):
            if board[i][j] == 2 or board[i][j] == 0:
                check = False
                break
    return check

def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 처음부터 홈이 없으면 True 리턴
    fullboard = [[1]*n for _ in range(n)]
    if fullboard == lock: return True

    for i in range(m+n-1):
        for j in range(m+n-1):
            for _ in range(4):
                key = turn(key,m)  # key를 90도 회전
                board = try_open(i,j,m,n,key,lock) # (2(m-1)+n)x(2(m-1)+n) 모양의 보드를 만들고 i,j에 key를 넣으면서 lock의 값과 더함
                if unlock(board, m,n) == True: return True # lock 부분의 값이 모두 1이면 자물쇠를 열 수 있으므로 True 리턴
    
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]),True)
print(solution([[0,1],[1,0]], [[0,1,0],[1,0,0],[0,0,1]]), False)