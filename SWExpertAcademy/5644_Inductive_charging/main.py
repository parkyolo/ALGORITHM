from collections import deque
T = int(input())

dx = [0, 0, 1, 0, -1] # 이동X, 상, 우, 하, 좌
dy = [0, -1, 0, 1, 0]
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    moving_a = list(map(int, input().strip().split()))
    moving_b = list(map(int, input().strip().split()))
    bc = list(list(map(int, input().split())) for _ in range(A))

    map_ = [[[] for _ in range(12)] for _ in range(12)]

    for i in range(A): # map에 bc의 index를 저장
        x, y, c, p = bc[i]
        queue = deque()
        v = set()
        map_[y][x].append(i)
        queue.append((x, y))
        v.add((x, y))
        for j in range(c):
            new_queue = deque()
            while queue:
                cx, cy = queue.popleft()
                for k in range(1, 5):
                    nx, ny = cx+dx[k], cy+dy[k]
                    if nx < 1 or nx > 10 or ny < 1 or ny > 10 or (nx, ny) in v: continue
                    map_[ny][nx].append(i)
                    new_queue.append((nx, ny))
                    v.add((nx, ny))
            queue = new_queue

    def get_power(arr): # 위치의 최대 충전량과 bc의 index를 반환
        power = 0
        idx = -1
        if arr:
            for i in arr:
                if bc[i][3] > power:
                    power = bc[i][3]
                    idx = i
        return power, idx

    ax, ay, bx, by = 1, 1, 10, 10
    charge = get_power(map_[ay][ax])[0] + get_power(map_[by][bx])[0]
    for i in range(M):
        ax += dx[moving_a[i]]
        ay += dy[moving_a[i]]
        bx += dx[moving_b[i]]
        by += dy[moving_b[i]]

        if not map_[ay][ax] and not map_[by][bx]: continue # bc에 접속할 수 없을 때
        ap, ai = get_power(map_[ay][ax]) # A의 최대 충전량과 접속한 bc의 index
        bp, bi = get_power(map_[by][bx]) # B의 최대 충전량과 접속한 bc의 index
        if ai == bi and ai != -1: # 같은 bc일 때
            if len(map_[ay][ax]) == 1 and len(map_[by][bx]) == 1: # 해당 bc만 접속할 수 있을 때
                charge += ap # 충전량을 균등하게 분배
            else: # 범위 안에 다른 bc가 있을 때
                sa, sb = 0, 0 # 두 번째로 큰 충전량
                if len(map_[ay][ax]) > 1:
                    for j in map_[ay][ax]:
                        if j != ai and bc[j][3] > sa:
                            sa = bc[j][3]
                if len(map_[by][bx]) > 1:
                    for j in map_[by][bx]:
                        if j != bi and bc[j][3] > sb:
                            sb = bc[j][3]
                charge += ap + max(sa, sb) # 최대 충전량 + 두 번째로 큰 충전량
        else:
            charge += ap + bp

    print("#"+str(test_case)+" "+str(charge))