r, c, t = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

air_cleaner = [] # 공기청정기의 행의 위치
for i in range(r):
    for j in range(c):
        if table[i][j] == -1:
            air_cleaner.append(i)
da = [[-1, 0, 1], [1, r-1, -1]] # 순환하는 방향

for _ in range(t):
    # 미세먼지 확산
    spread = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if table[i][j] > 0:
                temp = 0
                for k in range(4):
                    if 0 <= i+di[k] < r and 0 <= j+dj[k] < c and table[i+di[k]][j+dj[k]] != -1:
                        spread[i+di[k]][j+dj[k]] += table[i][j] // 5
                        temp += table[i][j] // 5
                table[i][j] -= temp
    # 기존의 미세먼지 값과 더하기
    for i in range(r):
        for j in range(c):
            table[i][j] += spread[i][j]
    # 공기청정기 작동
    for idx, v in enumerate(air_cleaner):
        for i in range(v+da[idx][0], da[idx][1], da[idx][0]):
            table[i][0] = table[i+da[idx][0]][0]

        for i in range(0, c-1):
            table[da[idx][1]][i] = table[da[idx][1]][i+1]
   
        for i in range(da[idx][1], v, da[idx][2]):
            table[i][c-1] = table[i+da[idx][2]][c-1]

        for i in range(c-1, 1, -1):
            table[v][i] = table[v][i-1]
        table[v][1] = 0

print(sum([sum(line) for line in table])+2)