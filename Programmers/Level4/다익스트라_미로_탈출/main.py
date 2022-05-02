import heapq
import sys
INF = sys.maxsize

def get_flag(cur_node, next_node, cur_state, trap_idx):
    is_cur_trap, is_next_trap = False, False
    if cur_node in trap_idx: # 현재 그래프가 cur_node가 함정인 상태를 담고 있으면 True
        is_cur_trap = (cur_state & (1 << trap_idx[cur_node])) > 0
    if next_node in trap_idx: # 현재 그래프가 next_node가 함정인 상태를 담고 있으면 True
        is_next_trap = (cur_state & (1 << trap_idx[next_node])) > 0

    return is_cur_trap == is_next_trap # 둘 다 함정이거나 둘 다 함정이 아니면 정방향 노드를 방문


def solution(n, start, end, roads, traps):
    graph_state = [[INF for _ in range(2**len(traps))] for _ in range(n+1)] # 노드와 그래프의 상태
    trap_idx = {t:i for i, t in enumerate(traps)} # 함정에 0부터 번호 붙이기
    graph = [[] for _ in range(n+1)] # 정방향, 역방향 간선을 모두 저장
    for road in roads:
        graph[road[0]].append([road[1], road[2], True]) # 정방향
        graph[road[1]].append([road[0], road[2], False]) # 역방향
    
    heap = []
    heapq.heappush(heap, [0, start, 0]) # 시간, 현재 노드, 현재 그래프 상태
    
    graph_state[0][start] = 0 # 첫 번째 노드
    while heap:
        time, cur_node, cur_state = heapq.heappop(heap)
        if cur_node == end: return time # 도착

        for next_node, w, flag in graph[cur_node]:
            if get_flag(cur_node, next_node, cur_state, trap_idx) != flag: continue # 방문할 수 없는 방향이면 continue
            
            next_state = cur_state ^ (1 << trap_idx[next_node]) if next_node in trap_idx else cur_state # 다음 노드가 함정이면 그래프 상태 변환
            if graph_state[next_node][next_state] <= time+w: continue 
            graph_state[next_node][next_state] = time+w # 처음 방문했거나 더 작은 값일 때 갱신
            heapq.heappush(heap, (time+w, next_node, next_state))
            
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]), 4)