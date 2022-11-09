import heapq

def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)

    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
        
    intensity = [10000001 for _ in range(n+1)]  # intensity[i] : 출발점 중 하나에서 i까지의 최소 intensity
    
    
    # 모든 출발점에서 모든 지점까지 최소 intensity를 구하는 함수
    def dijkstra(start): 
        queue = []
        heapq.heappush(queue, (0, start)) # 노드, intensity

        intensity[start] = 0

        while queue:
            dist, cur_node = heapq.heappop(queue)
            if cur_node in summits: continue # 산봉우리 도착
            
            if intensity[cur_node] < dist: continue

            for next_node, weight in graph[cur_node]:
                if next_node in gates: continue
                next_dist = max(dist, weight)
                if intensity[next_node] <= next_dist: continue
                intensity[next_node] = next_dist
                heapq.heappush(queue, (next_dist, next_node))

    for gate in gates:
        dijkstra(gate)

    answer = [0, 10000001]

    for summit in summits:
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
        elif intensity[summit] == answer[1]:
            answer[0] = min(answer[0], summit)
            
    return answer