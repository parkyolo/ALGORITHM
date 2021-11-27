from collections import deque

n, m = map(int, input().strip().split())
network = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    network[b-1].append(a-1)

answer = []
max_cnt = 0
for i in range(n):
    queue = deque()
    v = set()
    queue.append(i)
    v.add(i)
    while queue:
        bb = queue.popleft()
        for aa in network[bb]:
            if aa not in v:
                v.add(aa)
                queue.append(aa)
    cnt = len(v)
    if cnt > max_cnt:
        max_cnt = cnt
        answer = []
        answer.append(str(i+1))
    elif cnt == max_cnt:
        answer.append(str(i+1))

print(' '.join(answer))