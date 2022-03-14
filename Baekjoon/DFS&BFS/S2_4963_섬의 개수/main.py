from collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: exit() # 입력으로 0 0 이 들어오면 종료
    island = []
    for _ in range(h):
        island.append(list(map(int, input().split())))
    v = [[0 for _ in range(w)] for _ in range(h)]
    cnt = 0

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(h):
        for j in range(w):
            # 새로운 섬
            if island[i][j] == 1 and v[i][j] == 0:
                queue = deque()
                queue.append([i,j])
                v[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    # 8방향 탐색
                    for d in range(8):
                        if 0 <= x + dx[d] < h and 0 <= y + dy[d] < w:
                            if island[x + dx[d]][y + dy[d]] == 1 and v[x + dx[d]][y + dy[d]] == 0:
                                queue.append([x + dx[d], y + dy[d]])
                                v[x + dx[d]][y + dy[d]] = 1 # 방문 체크
                cnt += 1
    print(cnt)