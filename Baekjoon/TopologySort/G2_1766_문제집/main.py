import heapq

N, M = map(int, input().split())
graph = {i:[[],[]] for i in range(1, N+1)} # 노드 i: [부모 노드], [자식 노드]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][1].append(B)
    graph[B][0].append(A)

heap = []
answer = []
for key, val in graph.items():
    parents, children = val
    if not parents: # 진입차수가 0인 정점을 큐에 삽입
        heapq.heappush(heap, key)


while len(answer) < N:
    root = heapq.heappop(heap) # 큐에서 원소를 꺼냄
    answer.append(root) 
    for child in graph[root][1]:
        graph[child][0].remove(root) # 연결된 간선 제거
        if not graph[child][0]: # 간선 제거 후 진입차수가 0이 된 정점을 큐에 삽입
            heapq.heappush(heap, child)

for a in answer:
    print(a, end=' ')