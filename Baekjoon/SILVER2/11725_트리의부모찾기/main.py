from collections import deque

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    i, j = map(int, input().strip().split())
    tree[i-1].append(j-1)
    tree[j-1].append(i-1)

parent = [0 for _ in range(n-1)]
queue = deque()
for i in tree[0]:
    queue.append(i)
    parent[i-1] = 1

while queue:
    j = queue.popleft()
    for i in tree[j]:
        if i != 0 and parent[i-1] == 0:
            # 다음 노드i를 queue에 넣으면서 parent[i-1]에 j+1 체크
            queue.append(i)
            parent[i-1] = j+1

for p in parent:
    print(p)