from collections import deque

answer = 0
n, m = map(int, input().strip().split())
tree = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().strip().split())
    tree[u-1][v-1] = 1
    tree[v-1][u-1] = 1

v = set()
queue = deque()
for i in range(n):
    if i not in v:
        queue.append(i)
        v.add(i)
        while queue:
            x = queue.popleft()
            for y in range(n):
                if tree[x][y] == 1 and y not in v:
                    queue.append(y)
                    v.add(y)
        answer += 1
print(answer)