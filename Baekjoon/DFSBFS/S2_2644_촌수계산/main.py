from collections import deque

n = int(input())
s, e = map(int, input().strip().split())
m = int(input())

rel = [[] for _ in range(n+1)]
for _ in range(m):
    p, c = map(int, input().strip().split())
    rel[p].append(c)
    rel[c].append(p)

queue = deque([(s, 0)]) # 시작 노드, 거리
visited = set()         # 방문 체크 셋
visited.add(s)

answer = -1
while queue:
    cur_node, cnt = queue.popleft()
    
    if cur_node == e:
        answer = cnt
        break
    
    for next_node in rel[cur_node]:
        if next_node not in visited:
            visited.add(next_node)
            queue.append((next_node, cnt + 1))

print(answer)