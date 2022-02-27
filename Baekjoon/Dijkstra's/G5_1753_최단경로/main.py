import sys
import heapq

INF = sys.maxsize
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)] # graph[u] : (u에서 갈 수 있는 정점 v1와 가중치 w1), (v2, w2), ...
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dijk = [INF for _ in range(V+1)]
dijk[K] = 0
queue = []
heapq.heappush(queue, [0, K])
while queue:
    dist, q = heapq.heappop(queue)
    for u, w in graph[q]:
        if dist + w < dijk[u]: # 거리가 갱신될 때
            dijk[u] = dist + w
            heapq.heappush(queue, [dist+w, u])
for i in range(1, V+1):
    if dijk[i] == INF: print('INF')
    else: print(dijk[i])