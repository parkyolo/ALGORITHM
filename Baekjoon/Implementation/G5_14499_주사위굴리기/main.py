n, m, x, y, k = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(n)]
cmd = list(map(int, input().split()))

dx = [-1, 0, 0, -1, 1]
dy = [-1, 1, -1, 0, 0]
dm = [[], [[1,2], [1,1], [1,0]], [[1,0], [1,1], [1,2]], [[0,1], [1,1], [2,1]], [[2,1], [1,1], [0,1]]] # 방향이 i일 때 dm[i] : 주사위의 값이 바뀌는 순서

dice = [[0 for _ in range(3)] for _ in range(4)]
for c in cmd:
    if 0 <= x+dx[c] < n and 0 <= y+dy[c] < m:
        x += dx[c]
        y += dy[c]

        temp = dice[3][1] # dice[3][1]은 주사위의 바닥면, 값이 항상 변함
        cx, cy = 3, 1
        for i in range(3): # 주사위를 i방향으로 굴렸을 때 주사위의 값들을 변경
            nx, ny = dm[c][i]
            dice[cx][cy] = dice[nx][ny]
            cx, cy = nx, ny
        dice[cx][cy] = temp

        if map_[x][y] == 0: # 이동한 칸이 0일 때
            map_[x][y] = dice[3][1]
        else: # 0이 아닐 때
            map_[x][y], dice[3][1] = 0, map_[x][y]

        print(dice[1][1]) # 상단에 쓰여 있는 값