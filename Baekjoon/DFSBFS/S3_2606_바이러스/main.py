from collections import deque

n = int(input())  # 컴퓨터의 수
e = int(input())  # 연결된 컴퓨터 쌍의 수

visited = [0 for _ in range(n+1)]   # 방문 체크 배열
visited[1] = 1                      # 1번 컴퓨터부터 탐색 시작

network = [[] for _ in range(n+1)]  # 연결 리스트

# 연결된 컴퓨터의 번호를 연결 리스트에 추가
for _ in range(e):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

# 1번 컴퓨터와 연결된 컴퓨터 탐색
queue = deque([1])
while queue:
    cur_com = queue.popleft()
    for next_com in network[cur_com]:
        if not visited[next_com]:
            visited[next_com] = 1
            queue.append(next_com)
            
print(sum(visited)-1) # 1번 컴퓨터를 제외하고 1번 컴퓨터와 연결된 컴퓨터의 수 출력
