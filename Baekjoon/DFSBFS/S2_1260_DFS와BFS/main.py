from collections import deque

n, m, v = map(int, input().split())
dfs_v = [0 for _ in range(n)]
bfs_v = [0 for _ in range(n)]

# 간선 정보 저장
edges = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    edges[i-1][j-1] = 1
    edges[j-1][i-1] = 1

# DFS 구현
def dfs(s,ans):
    if dfs_v[s] == 1: return
    dfs_v[s] = 1
    ans += str(s+1) +" "
    for node in range(n):
        if edges[s][node] == 1 and dfs_v[node] == 0:
            ans = dfs(node, ans)
    return ans
print(dfs(v-1, "").rstrip())

# BFS 구현
queue = deque([v-1])
bfs = ""
while queue:
    q = queue.popleft()
    if bfs_v[q] == 1: continue
    bfs_v[q] = 1
    bfs += str(q+1) +" "
    for node in range(n):
        if edges[q][node] == 1 and bfs_v[node] == 0:
            queue.append(node)
print(bfs.rstrip())