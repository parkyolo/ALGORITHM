n = int(input())
YN = []
for _ in range(n):
    YN.append(input())

y_f = [set() for _ in range(n)] # y_f[i] : i와 친구인 사람
n_f = [set() for _ in range(n)] # n_f[i]: i와 친구가 아닌 사람

# A와 B가 친구인지 아닌지는 대각선을 기준으로 대칭되므로 절반만 탐색
for i in range(n):
    rel_i = YN[i]
    for j in range(i):
        if rel_i[j] == 'Y':
            y_f[i].add(j)
            y_f[j].add(i)
        else:
            n_f[i].add(j)
            n_f[j].add(i)

max_cnt = -1
for i in range(n):
    cnt = len(y_f[i]) # 이미 친구인 사람 수
    for j in n_f[i]: # 친구가 아닌 사람들 중
        if len(y_f[i] & y_f[j]) > 0: # 겹치는 친구가 있는 사람
            cnt += 1
    if cnt > max_cnt: max_cnt = cnt
print(max_cnt)