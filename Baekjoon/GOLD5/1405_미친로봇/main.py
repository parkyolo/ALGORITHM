n, ea, we, so, no = map(int, input().split())
v = set([(n, n)]) # 방문 체크
direc_pct = [ea*0.01, we*0.01, so*0.01, no*0.01] # 방향으로 이동할 확률
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0

def dfs(x, y, v, move, pct):
    global n, result
    if move == n: result += pct; return; # n번 이동하면 종료
    for i in range(4):
        if direc_pct[i] and (x+dx[i],y+dy[i]) not in v: # 확률이 존재하고 아직 방문하지 않은 위치이면
                temp = set([(x+dx[i], y+dy[i])])
                dfs(x+dx[i], y+dy[i], v | temp , move+1, pct*direc_pct[i])

dfs(n, n, v, 0, 1)
print(result)