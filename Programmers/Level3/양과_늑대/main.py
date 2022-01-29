def solution(info, edges):
    answer = 0
    tree = [[] for _ in range(len(info))] # i 노드의 자식 노드는 tree[i]
    for edge in edges:
        tree[edge[0]].append(edge[1])

    stack = [[0, 0, 0, set()]] 
    while stack:
        cur, sheep, wolf, nodes = stack.pop() # 현재 위치, 현재까지 모은 양의 수, 늑대의 수, 다음으로 방문할 수 있는 노드 집합
        sheep += info[cur] ^ 1 # xor 연산 (info[cur]이 0이면 +1, 1이면 +0)
        wolf += info[cur]
        if wolf >= sheep: continue # 늑대가 양보다 많다면 continue
        if sheep > answer: answer = sheep # sheep의 수 갱신
        nodes = nodes | set(tree[cur]) # 현재 노드의 자식 노드를 '다음으로 방문할 수 있는 노드 집합'에 추가
        for node in nodes:
            stack.append([node, sheep, wolf, nodes-set([node])]) # 다음으로 방문할 node를 집합에서 제거
    return answer

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]), 5)
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]), 5)