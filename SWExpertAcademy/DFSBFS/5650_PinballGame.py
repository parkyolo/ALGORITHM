'''
5650. [모의 SW 역량테스트] 핀볼 게임
(https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo&categoryId=AWXRF8s6ezEDFAUo&categoryType=CODE&problemTitle=5650&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

1. table[i][j] == 0일 때, 상하좌우로 움직이는 경우를 queue에 넣음
2. x, y가 출발위치로 돌아오거나 table[x][y] == -1이면 continue
3. 블록과 부딪히면 방향 전환, cnt+1
4. 웜홀과 만나면 반대쪽 웜홀로 위치 전환
'''

from collections import deque

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
table, wormhole = [], [] # 게임판, 웜홀의 위치
cdir = [-1, [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0] ,[1, 0, 3, 2]] # cdir[i][j] : j 방향에서 i번 블록과 부딪혔을 때 전환되는 방향

def game(start_x, start_y):
    queue = deque()
    max_cnt = 0
    for i in range(4):
        queue.append((start_x+dx[i], start_y+dy[i], i, 0))

    while queue:
        x, y, dir, cnt = queue.popleft()
        block = table[x][y]
        if (x == start_x and y == start_y) or block == -1: # 출발 위치로 돌아오거나 블랙홀에 빠진 경우
            if max_cnt < cnt:
                max_cnt = cnt
            continue
        if 1 <= block <= 5: # 블록과 부딪힐 때
            cnt += 1
            dir = cdir[block][dir]
        elif 6 <= block <= 10: # 웜홀에 빠질 때
            for i, j in wormhole[block]:
                if i != x or j != y:
                    x, y = i, j
                    break
        queue.append((x+dx[dir], y+dy[dir], dir, cnt))

    return max_cnt

for test_case in range(1, T+1):
    ans, table, wormhole = 0, [], [-1, -1, -1, -1, -1, -1, [], [], [], [], []]
    n = int(input())

    table.append([5 for _ in range(n+2)]) # 패딩
    for _ in range(n):
        table.append([5]+list(map(int, input().strip().split()))+[5])
    table.append([5 for _ in range(n+2)])

    for i in range(1, n+1): # 웜홀 위치 저장
        for j in range(1, n+1):
            if 6 <= table[i][j] <= 10:
                wormhole[table[i][j]].append((i,j))

    for i in range(1, n+1):
        for j in range(1, n+1):
            if table[i][j] == 0: # 블록, 웜홀 또는 블랙홀이 없는 위치에서 출발
                cnt = game(i, j)
                if cnt > ans:
                    ans = cnt
    print('#'+str(test_case)+" "+str(ans))