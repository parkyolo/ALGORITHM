from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

queue = deque()
queue.append([[r1, c1], 0])
visited = [[False for _ in range(n)] for _ in range(n)]

# 데스 나이트가 이동할 수 있는 거리
di = [-2, -2, 0, 0, 2, 2]
dj = [-1, 1, -2, 2, -1, 1]

while queue:
    horse, cnt = queue.popleft()
    # 현재 위치
    r = horse[0]
    c = horse[1]

    if visited[r][c] == True: continue
    visited[r][c] = True

    # 데스 나이트가 (r2, c2)로 이동하는 최소 이동 횟수 cnt를 출력
    if r == r2 and c == c2:
        print(cnt)
        break
    
    # 데스 나이트를 움직임
    for i in range(6):
        if n > r+di[i] >= 0 and n > c+dj[i] >= 0 and visited[r+di[i]][c+dj[i]] == False:
            queue.append([[r+di[i], c+dj[i]], cnt+1])

# 데스 나이트가 (r2, c2)로 이동할 수 없는 경우
if visited[r2][c2] == False:
    print(-1)