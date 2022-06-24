from collections import deque

M, N = map(int, input().split()) # 상자의 가로, 세로 칸의 수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(tomatos):
    days = 1
    queue = deque() # (익은 토마토의 위치, 일수)
    for x in range(N):
        for y in range(M):
            if tomatos[x][y] == 1: # 익은 토마토의 위치와 일수를 큐에 넣음
                queue.append((x, y, 1))

    while queue:
        x, y, day = queue.popleft()
        for d in range(4): # 인접한 토마토 탐색
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or nx >= N or ny <0 or ny >= M or tomatos[nx][ny]: continue # 범위를 벗어났거나 익지 않은 토마토가 아니면 continue
            tomatos[nx][ny] = 1
            queue.append((nx, ny, day+1))
            days = max(day, days) # 일수 갱신
                
    non_riped = sum([1 for y in range(M) for x in range(N) if tomatos[x][y] == 0]) # 탐색이 끝난 후 익지 않은 토마토 개수
    if non_riped == 0: # 토마토가 모두 익었을 때
        if days == 1: # 저장될 때부터 모든 토마토가 익어있는 상태
            return 0
        else:
            return days
    else: # 토마토가 모두 익지 못할 때
        return -1

def main():
    tomatos = list(list(map(int, input().split())) for _ in range(N))
    print(bfs(tomatos))
    return

if __name__ == "__main__":
    main()