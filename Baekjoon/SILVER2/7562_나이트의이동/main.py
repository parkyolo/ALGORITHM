from collections import deque

t = int(input())
for _ in range(t):
    l = int(input())
    cur_x, cur_y = map(int, input().split())
    des_x, des_y = map(int, input().split())

    dx = [-1, -2, -2, -1, 1, 2, 1, 2]
    dy = [-2, -1, 1, 2, -2, -1, 2, 1]

    v = [[0 for _ in range(l)] for _ in range(l)]
    queue = deque([[cur_x, cur_y]])
    while queue:
        x, y = queue.popleft()
        if x == des_x and y == des_y:
            print(v[x][y])
            break
        for d in range(8):
            if 0 <= x + dx[d] < l and 0 <= y + dy[d] < l and v[x + dx[d]][y + dy[d]] == 0:
                queue.append([x + dx[d], y + dy[d]])
                v[x + dx[d]][y + dy[d]] = v[x][y] + 1