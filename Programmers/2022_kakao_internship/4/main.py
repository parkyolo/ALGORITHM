from collections import deque
intensity, summit = 0, 0

def get_intensity(s, i):
    global summit, intensity
    if i < intensity:
        summit, intensity = s, i
    elif i == intensity:
        summit = min(summit, s)

def find(n, start, gates, summits, graph):
    queue = deque()
    queue.append([start, 0]) # 노드, intensity

    v = [0 for _ in range(n+1)]
    v[start] = 1

    while queue:
        cur_node, time = queue.popleft()
        if cur_node in summits:
            get_intensity(cur_node, time)
            continue
        for node, weight in graph[cur_node]:
            if node in gates or v[node]: continue
            queue.append([node, max(time,weight)])
            if node not in summits: v[node] = 1

def solution(n, paths, gates, summits):
    global summit, intensity
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
        intensity = max(intensity, w)

    for gate in gates:
        find(n, gate, gates, summits, graph)
            
    return [summit, intensity]

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]), [5, 3])
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]), [3, 4])
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]), [5, 1])
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]), [5, 6])