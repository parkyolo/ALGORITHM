from collections import deque

n, m, k, x = map(int, input().strip().split())
cities = [[] for _ in range(n)]

for _ in range(m):
    s, a = map(int, input().strip().split())
    cities[s-1].append(a-1) # 인접 도시 추가

queue = deque()
v = set()

answer = []
queue.append([x-1,0]) # [도시, 거리]
v.add(x-1) # 방문 체크
while queue:
    city, cnt = queue.popleft()
    if cnt == k:
        answer.append(city+1)
        continue # cnt가 k보다 커지지 않게
    for c in cities[city]:
        if c not in v:
            queue.append([c, cnt + 1])
            v.add(c)

if len(answer) > 0:
    answer.sort()
    for a in answer:
        print(a)
else:
    print(-1)