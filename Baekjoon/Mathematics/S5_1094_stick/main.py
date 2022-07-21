import heapq

X = int(input())
queue = [64]
sum_ = 64

while sum_ > X:
    stick = heapq.heappop(queue)
    stick //= 2
    heapq.heappush(queue, stick)
    if sum_ - stick >= X:
        sum_ -= stick
    else:
        heapq.heappush(queue, stick)

print(len(queue))