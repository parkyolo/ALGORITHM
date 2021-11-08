r, c = map(int, input().split())
pasture = []
for _ in range(r):
    pasture.append(list(input()))

# 양의 좌표
sheep = ([[i,j] for i in range(r) for j in range(c) if pasture[i][j] == 'S'])

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for s_r, s_c in sheep:
    for d in range(4):
        if -1 < s_r+di[d] < r and -1 < s_c+dj[d] < c:
            # 양의 상하좌우에 늑대가 있는지 검사
            if pasture[s_r+di[d]][s_c+dj[d]] == 'W':
                print(0)
                exit()
            # 울타리 설치
            elif pasture[s_r+di[d]][s_c+dj[d]] == '.':
                pasture[s_r+di[d]][s_c+dj[d]] = 'D'

print(1)
for i in range(r):
    print(''.join(pasture[i]))
