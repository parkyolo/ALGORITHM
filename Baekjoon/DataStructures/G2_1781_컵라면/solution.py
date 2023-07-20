import heapq

n = int(input())
info = []
queue = []

for i in range(n):
    d, c = map(int, input().split())
    info.append([d, c])

info.sort(key = lambda x:(x[0], -x[1]))

for d, c in info:
    if d > len(queue):
        heapq.heappush(queue, c)
    elif c > queue[0]:
        heapq.heappop(queue)
        heapq.heappush(queue, c)

print(sum(queue))