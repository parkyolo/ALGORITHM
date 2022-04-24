N = int(input())
M = int(input())
graph = list(list(map(int, input().split())) for _ in range(M))
graph.sort(key=lambda x:x[2])

set_ = [i for i in range(N+1)]

def find(u):
    if u != set_[u]:
        set_[u] = find(set_[u])
    return set_[u]

def union(u,v):
    root1 = find(u)
    root2 = find(v)
    set_[root2] = root1

cost = 0
for a, b, c in graph:
    if find(a) == find(b): continue
    union(a, b)
    cost += c

print(cost)