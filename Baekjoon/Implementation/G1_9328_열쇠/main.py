from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
doors = dict() # {열쇠 : 문의 위치}

def bfs(map_, keys, start, h, w):
    global answer, doors
    queue = deque([start])

    # . : 빈 공간, * : 벽, $ : 문서, A-Z : 문, a-z : 열쇠, - : 방문 체크
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w: continue # 범위를 벗어날 때
            ncur = map_[nx][ny]
            if ncur == '-' or ncur == '*':continue # 방문했거나 벽일 때
            if ncur.isupper() and ncur.lower() not in keys: # 문을 열 수 없을 때
                if ncur.lower() in doors: doors[ncur.lower()].append((nx, ny))
                else: doors[ncur.lower()] = [(nx, ny)]
                continue 
            if ncur == '$': answer += 1 # 문서일 때
            elif ncur.islower(): # 열쇠일 때
                keys.add(ncur)
                if ncur in doors: # 방문했지만 못 열었던 문이 있으면
                    for door in doors[ncur]:
                        queue.append(door) # 큐에 추가
                    del doors[ncur]
            map_[nx][ny] = '-' # 방문 체크
            queue.append((nx, ny)) # 큐에 추가

def init(r, c, map_, keys, start_point):
    global answer, doors
    cur = map_[r][c]
    if cur.isupper() and cur.lower() not in keys: # 문을 열 수 없을 때
        if cur.lower() in doors: doors[cur.lower()].append((r, c))
        else: doors[cur.lower()] = [(r, c)]
        return
    if cur == '$': answer += 1 # 문서일 때
    elif cur.islower(): keys.add(cur) # 열쇠일 때
    start_point.append((r, c))
    map_[r][c] = '-'

def solution(h, w):
    # . : 빈 공간, * : 벽, $ : 문서, A-Z : 문, a-z : 열쇠, - : 방문 체크
    map_ = list(list(input()) for _ in range(h))
    keys = input()
    if keys == "0": keys = set() # 열쇠를 가지고 있지 않은 경우
    else: keys = set(keys)

    start_point = [] # 가장자리 중 벽이 아닌 곳
    for i in range(h):
        if map_[i][0] != '*': init(i, 0, map_, keys, start_point)
        if map_[i][w-1] != '*' : init(i, w-1, map_, keys, start_point)
    for j in range(w):
        if map_[0][j] != '*': init(0, j, map_, keys, start_point)
        if map_[h-1][j] != '*' : init(h-1, j, map_, keys, start_point)

    for sp in start_point:
        bfs(map_, keys, sp, h, w)

def main():
    global answer, doors
    T = int(input())
    for _ in range(T):
        answer, doors = 0, dict() # 초기화
        h, w = map(int, input().split())
        solution(h, w)
        print(answer)

if __name__ == "__main__":
    main()