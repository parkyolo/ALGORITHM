import heapq
import sys
def solution(n, s, a, b, fares):
    INF = sys.maxsize
    edges = [[] for _ in range(n+1)]
    for d,c,f in fares:
        edges[d].append([c,f])
        edges[c].append([d,f])
    
    # 출발지점 s부터 모든 지점까지의 거리
    dijk = [INF for _ in range(n+1)]
    dijk[s] = 0
    queue = []
    heapq.heappush(queue, [0, s])
    while queue:
        dist, q = heapq.heappop(queue)
        for u, w in edges[q]:
            if dist + w < dijk[u]:
                dijk[u] = dist + w
                heapq.heappush(queue, [dist+w, u])
    
    answer = dijk[a] + dijk[b]
    
    # 모든 지점 i부터 a, b까지의 거리
    for i in range(1, n+1):
        arr = [INF for _ in range(n+1)]
        arr[i] = 0
        dists = []
        heapq.heappush(dists, [0, i])
        while dists:
            dist, d = heapq.heappop(dists)
            for u, w in edges[d]:
                if dist + w < arr[u]:
                    arr[u] = dist + w
                    heapq.heappush(dists, [dist+w, u])
        if dijk[i] + arr[a] + arr[b] < answer:
            answer = dijk[i] + arr[a] + arr[b]
    
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]),82)
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]),14)
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]),18)