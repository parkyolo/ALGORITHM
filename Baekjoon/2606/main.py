from collections import deque

n = int(input())
connect = int(input())
v = [0 for _ in range(n)]
v[0] = 1
network = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(connect):
    i,j = map(int, input().split())
    network[i-1][j-1] = 1
    network[j-1][i-1] = 1
queue = deque()
answer = 0
for i in range(n):
    if network[0][i] == 1:
        queue.append(i)
while queue:
    i = queue.popleft()
    if v[i] == 1: continue
    v[i] = 1
    answer += 1
    for j in range(n):
        if v[j] != 1:
            if network[i][j] ==1:
                queue.append(j)
print(answer)
