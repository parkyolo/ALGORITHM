n = int(input())
board = [0 for _ in range(n)]
v = [False for _ in range(n)]
cnt = 0

def check(m):
    for i in range(m): 
        if abs(board[m] - board[i]) == m -i:
            return False
    return True

def nqueen(m):
    global cnt, n, v
    if m == n:
        cnt += 1
        return
    for i in range(n):
        if v[i]: continue

        board[m] = i
        if check(m):
            v[i] = True
            nqueen(m+1)
            v[i] = False


nqueen(0)
print(cnt)