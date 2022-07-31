import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

def main():
    n, m = map(int, input().split())
    dist = [[INF for _ in range(n+1)] for _ in range(n+1)] # 거리 배열
    table = [[INF for _ in range(n+1)] for _ in range(n+1)] # 첫 번째 집하장

    for _ in range(m):
        a, b, d = map(int, input().split())

        dist[a][b] = d
        dist[b][a] = d

        table[a][b] = b
        table[b][a] = a
    
    for i in range(1, n+1):
        dist[i][i] = 0
        table[i][i] = '-'
        queue = deque()
        for j in range(1, n+1):
            if dist[i][j] != 0 and dist[i][j] != INF: 
                queue.append((dist[i][j], j, j)) # 거리, 이전 노드, 첫 노드
        
        while queue:
            distance, pre_node, first_node = queue.popleft()
            for j in range(1, n+1):
                if dist[i][j] <= distance + dist[pre_node][j]: continue
                dist[i][j] = distance + dist[pre_node][j] # 최단 거리 갱신
                table[i][j] = first_node # 시작 점 기록
                queue.append((distance + dist[pre_node][j], j, first_node))

    for i in range(1, n+1):
        print(" ".join([str(t) for t in table[i][1:]]))

if __name__ == "__main__":
    main()