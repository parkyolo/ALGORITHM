from collections import deque

n, m = 0, 0
edges, parent = deque(), []
cnt = 0
road_cnt = []

def union_root(x, y):
    x = find_root(x)
    y = find_root(y)
    if x != y: parent[y] = x

def find_root(x):
    if x == parent[x]: return x
    else: return find_root(parent[x])

def kruskal():
    global edges, cnt

    next_edges = deque()
    while edges:
        node1, node2 = edges.popleft()
        if find_root(node1) == find_root(node2):
            next_edges.append([node1, node2])
            continue
        road_cnt[node1] += 1
        road_cnt[node2] += 1
        cnt += 1
        union_root(node1, node2)
    edges = next_edges

def main():
    global n, m, edges, parent, road_cnt
    n, m = map(int, input().split())
    matrix = list(list(input()) for _ in range(n))
    
    parent = [i for i in range(n)]
    road_cnt = [0 for _ in range(n)]
    for i in range(n):              # 1. 우선순위가 높은 노드 순으로 저장
        for j in range(i, n):
            if matrix[i][j] == 'Y':
                edges.append([i, j])
    
    if len(edges) < m:
        print(-1)                   # 2. edge의 개수가 m보다 작으면 문제의 조건을 만족할 수 없으므로 -1 출력
        return

    kruskal()                       # 3. MST 생성
    if cnt == n-1:                  # 4. MST의 노드의 수 cnt가 n-1이면 모든 노드가 연결되었다는 의미
        for _ in range(m-cnt):      # 5. m개의 도로를 연결하기 위해 m-cnt만큼 더 연결
            node1, node2 = edges.popleft()
            road_cnt[node1] += 1
            road_cnt[node2] += 1
        print(*road_cnt)            # 6. 각 노드마다 연결된 edge의 수 출력
    else:
        print(-1)
    
if __name__ == "__main__":
    main()