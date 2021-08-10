from collections import deque

def dijkstra(graph):
    # 0과 road 간의 거리를 담을 dictionary
    distances = {i: 500001 for i in graph}
    distances[0] = 0
    queue = deque()
    queue.append([distances[0], 0])

    while queue:
        d, node = queue.popleft()

        if distances[node] < d:
            continue

        for dest, dist in graph[node]:
            new_dist = d+dist
            # 두 마을을 이었을 때의 거리가 더 짧으면 dist의 값을 바꿔줌
            if new_dist < distances[dest]:
                distances[dest] = new_dist
                queue.append([new_dist, dest])

    return distances

def solution(N, road, K):
    answer = 0

    # road를 graph에 넣음
    graph = {}
    for a, b, c in road:
        graph[a-1] = graph.get(a-1, []) + [(b-1, c)]
        graph[b-1] = graph.get(b-1, []) + [(a-1, c)]
            
    for i in range(N):
        if i not in graph:
            graph[i] = {}

    dist = dijkstra(graph)

    # K 이하의 시간에 배달이 가능한 마을의 개수를 count
    for v in dist.values():
        if v <= K:
            answer += 1

    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3),4)
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4),4)