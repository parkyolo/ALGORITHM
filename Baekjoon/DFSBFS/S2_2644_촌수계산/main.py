from collections import deque

n = int(input())
s, e = map(int, input().strip().split())
m = int(input())

rel = [[] for _ in range(n)]
for _ in range(m):
    p, c = map(int, input().strip().split())
    rel[p-1].append(c-1)
    rel[c-1].append(p-1)

v = set()
queue = deque()
queue.append([s-1, 0])
v.add(s-1)

while queue:
    cur, cnt = queue.popleft()
    if cur+1 == e:
        print(cnt)
        exit()
    for f in rel[cur]:
        if f not in v:
            v.add(f)
            queue.append([f, cnt + 1])
print(-1)