from collections import deque
n, m = map(int, input().split())
graph = [[set(), set()] for _ in range(n)]
for _ in range(m):
    A, B = map(int, input().split())
    graph[B-1][0].add(A-1)
    graph[A-1][1].add(B-1)

line = []

def topological_sort(): # 줄 세우기
    queue = deque()
    for idx in range(n): # 진입 차수가 0인 정점 찾기
        if len(graph[idx][0]) == 0:
            queue.append(idx)
    
    while queue:
        x = queue.popleft()
        line.append(str(x+1))
        for v in graph[x][1]:
            graph[v][0].remove(x) # 연결된 간선 제거
            if len(graph[v][0]) == 0: # 간선 제거 후 진입 차수가 0이 되면 queue에 삽입
                queue.append(v)

topological_sort()
print(' '.join(line))