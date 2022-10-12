from collections import deque
import sys

N, board = 0, []
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
minLength = sys.maxsize

def numbering(): # 섬마다 각기 다른 번호를 부여하는 함수
    num = 2
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                queue = deque([[x, y]])
                board[x][y] = num
                while queue:
                    cx, cy = queue.popleft()
                    for d in range(4):
                        nx, ny = cx+dxy[d][0], cy+dxy[d][1]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                        if board[nx][ny] != 1: continue
                        board[nx][ny] = num
                        queue.append([nx, ny])
                num += 1

def bridging(): # 섬과 섬을 연결하는 가장 짧은 경로를 구하는 함수
    global minLength
    for x in range(N):
        for y in range(N):
            if board[x][y] > 1:
                num = board[x][y]
                queue = deque([[x, y, 0]])
                visited = [[0 for _ in range(N)] for _ in range(N)]
                visited[x][y] = 1
                while queue:
                    cx, cy, cnt = queue.popleft()
                    for d in range(4):
                        nx, ny = cx+dxy[d][0], cy+dxy[d][1]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]: continue  # 범위를 벗어났거나 이미 방문한 경우
                        if board[nx][ny] == num: continue                                       # 같은 섬인 경우
                        if cnt+1 > minLength: continue                                          # (nx, ny)로 이동했을 때 현재 minLength보다 커지는 경우
                        if board[nx][ny] > 0 and board[nx][ny] != num:                          # 최소 거리로 다른 섬에 도착한 경우
                            minLength = cnt # minLength 갱신
                            continue
                        queue.append([nx, ny, cnt+1])
                        visited[nx][ny] = 1

def main():
    global N, board
    N = int(input())
    board = list(list(map(int, input().split())) for _ in range(N))

    numbering() # 1. 섬마다 번호를 부여한다.
    bridging()  # 2. 번호가 다른 섬과의 최소 거리를 구한다.
    print(minLength)

if __name__ == "__main__":
    main()