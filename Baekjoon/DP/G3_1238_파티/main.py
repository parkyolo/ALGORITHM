import sys
import heapq
N, M, X = 0, 0, 0
INF = sys.maxsize

def dijkstra(time2i): # X에서 다른 모든 노드로 가는 데 걸리는 최단 시간
    shortest_time = [INF for _ in range(N)]
    shortest_time[X] = 0
    queue = [(X, 0)]

    while queue:
        node, time = heapq.heappop(queue)
        if shortest_time[node] < time: continue
        for next_node, next_time in time2i[node]:
            next_time += time
            if next_time < shortest_time[next_node]:
                shortest_time[next_node] = next_time
                heapq.heappush(queue, (next_node, next_time))

    return shortest_time

def main():
    global N, M, X
    N, M, X = map(int, input().split())
    X = X-1
    time2X = {i:[] for i in range(N)} # i에서 X로 가는 데 걸리는 시간을 구하기 위한 리스트
    time2i = {i:[] for i in range(N)} # X에서 i로 가는 데 걸리는 시간을 구하기 위한 리스트
    for _ in range(M):
        from_, to, time = map(int, input().split())
        time2X[to-1].append((from_-1, time))
        time2i[from_-1].append((to-1, time))
    
    i2X = dijkstra(time2X)
    X2i = dijkstra(time2i)

    answer = 0
    for time_i2X, time_X2i in zip(i2X, X2i):
        answer = max(answer, time_i2X + time_X2i)
    print(answer)

if __name__ == "__main__":
    main()