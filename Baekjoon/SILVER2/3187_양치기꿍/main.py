from collections import deque

n, m = map(int, input().split())
farm = [input() for _ in range(n)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

survive_sheep = 0
survive_wolves = 0
v = set()
for i in range(n):
    for j in range(m):
        if (farm[i][j] == 'v' or farm[i][j] == 'k') and (i,j) not in v: # 양이나 늑대가 있고 아직 방문하지 않았을 때
            queue = deque()
            wolves = 0 # 같은 울타리 영역 안의 늑대 수
            sheep = 0 # 같은 울타리 영역 안의 양 수
            queue.append([i,j])
            v.add((i,j)) # 방문 체크
            if farm[i][j] == 'v': wolves += 1
            elif farm[i][j] == 'k': sheep += 1
            while queue:
                now_i, now_j = queue.popleft()
                for k in range(4):
                    if 0 <= now_i+di[k] < n and 0 <= now_j+dj[k] < m:
                        if (farm[now_i+di[k]][now_j+dj[k]] == 'v' or farm[now_i+di[k]][now_j+dj[k]] == 'k') and (now_i+di[k], now_j+dj[k]) not in v: # 같은 울타리에 양이나 늑대가 있을 때
                            queue.append([now_i+di[k], now_j+dj[k]])
                            v.add((now_i+di[k], now_j+dj[k]))
                            if farm[now_i+di[k]][now_j+dj[k]] == 'v': wolves += 1
                            elif farm[now_i+di[k]][now_j+dj[k]] == 'k': sheep += 1
                        elif farm[now_i+di[k]][now_j+dj[k]] == '.' and (now_i+di[k], now_j+dj[k]) not in v: # 울타리 안일 때
                            queue.append([now_i+di[k], now_j+dj[k]])
                            v.add((now_i+di[k], now_j+dj[k]))
            if wolves < sheep: # 울타리 안에 양이 더 많을 때
                survive_sheep += sheep
            else: # 울타리 안에 양이 더 많지 않을 때
                survive_wolves += wolves
print(survive_sheep, survive_wolves)