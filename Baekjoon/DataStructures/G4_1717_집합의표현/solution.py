import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x: 
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    parent_x = find_parent(x)
    parent_y = find_parent(y)
    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y

for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal: # 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
    else:   # 합집합 연산
        union(a, b)