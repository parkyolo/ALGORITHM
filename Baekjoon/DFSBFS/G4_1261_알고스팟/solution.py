from collections import deque
import sys
INF = sys.maxsize

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def main():
    m, n = map(int, input().split())
    board = list(list(map(int, list(input()))) for _ in range(n))

    dist = [[INF for _ in range(m)] for _ in range(n)] # dist[x][y]: (x, y)로 이동하기 위해 부숴야 하는 벽의 개수
    dist[0][0] = 0
    queue = deque([(0, 0)])
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dxy[i][0], cy + dxy[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

            if dist[nx][ny] <= dist[cx][cy] + board[nx][ny]: continue

            dist[nx][ny] = dist[cx][cy] + board[nx][ny]
            queue.append((nx, ny))

    print(dist[n-1][m-1])


if __name__ == "__main__":
    main()