from collections import deque

def solution(n, vertex):
    answer = 0
    max_cnt = 0
    edges = [[] for _ in range(n)]
    visited = set() # list를 쓸 경우 시간 초과
    
    # 배열의 index는 출발 노드, 원소는 도착 노드
    for v in vertex:
        edges[v[0]-1].append(v[1]-1)
        edges[v[1]-1].append(v[0]-1)

    queue = deque([(0,0)])

    # BFS로 탐색
    while queue:
        node, cnt = queue.popleft()
        visited.add(node)
        if cnt > max_cnt:
            max_cnt = cnt
            answer = 1
        elif cnt == max_cnt:
            answer += 1
        # 방문하지 않은 연결 노드에 대해 거리+1해서 queue에 저장
        for e in edges[node]:
            if e not in visited:
                queue.append((e, cnt + 1))
                visited.add(e)

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
      3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
print(solution(2, [[1, 2]]), 1)
print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)