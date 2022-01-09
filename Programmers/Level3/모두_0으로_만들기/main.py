import sys
sys.setrecursionlimit(300000)
cnt = 0

def dfs(node, a, tree, v):
    global cnt
    v.add(node)

    for i in tree[node]:
        if i not in v:
            v.add(i)
            a[node] += dfs(i, a, tree, v)
    cnt += abs(a[node])

    return a[node]

def solution(a, edges):
    global cnt

    if sum(a) != 0: return -1

    n = len(a)
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    v = set()
    dfs(0, a, tree, v)

    return cnt

# print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]), 9)
# print(solution([0, 1, 0], [[0, 1], [1, 2]]), -1)
print(solution([-2, 8, -5, -5, -3, 0, 5, 2], [[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]]), 17)