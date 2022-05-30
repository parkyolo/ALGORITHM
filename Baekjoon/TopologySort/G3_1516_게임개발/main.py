from collections import deque

N = int(input())

cost = {i:0 for i in range(1, N+1)}
graph = {i:[[], []] for i in range(1, N+1)}
for i in range(1, N+1):
    arr = list(map(int, input().split()))
    cost[i] = arr[0]
    for j in range(1, len(arr)-1):
        graph[i][0].append(arr[j])
        graph[arr[j]][1].append(i)

queue = deque()
for key, val in graph.items():
    if not val[0]:
        queue.append(key)

dp = [cost[i] if i in cost else 0 for i in range(N+1)]
while queue:
    cur = queue.popleft()
    for next in graph[cur][1]:
        graph[next][0].remove(cur)
        dp[next] = max(dp[cur]+cost[next], dp[next])
        if not graph[next][0]:
            queue.append(next)

for i in range(1, N+1):
    print(dp[i])