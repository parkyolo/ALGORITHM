from collections import deque
V, tree = 0, []
answer, start_idx, visited = 0, 0, []

def input_():
    global V, tree
    V = int(input())
    tree = [[] for _ in range(V)]
    for _ in range(V):
        node_info = deque(list(map(int, input().split())))
        cur_node = node_info.popleft()-1
        while node_info:
            next_node = node_info.popleft()-1
            if next_node == -2: break
            distance = node_info.popleft()
            tree[cur_node].append((next_node, distance))

def dfs(node, dist_sum):
    global answer, start_idx
    if dist_sum > answer:
        start_idx = node
        answer = dist_sum
    answer = max(answer, dist_sum)
    for num, dist in tree[node]:
        if not visited[num]:
            visited[num] = True
            dfs(num, dist_sum+dist)
            visited[num] = False

def solution(start_idx):
    global answer, visited
    # dfs를 한 번 수행할 때마다 visited와 answer를 초기화
    visited = [False for _ in range(V)] # 방문 체크 배열
    answer = 0 # 트리의 지름
    visited[start_idx] = True
    dfs(start_idx, 0)


def main():
    global start_idx
    input_()

    start_idx = 0
    solution(start_idx) # 0에서 가장 먼 노드를 찾아서 start_idx 갱신
    solution(start_idx) # start_idx에서 가장 먼 노드를 찾는다.

    print(answer)

if __name__ == "__main__":
    main()