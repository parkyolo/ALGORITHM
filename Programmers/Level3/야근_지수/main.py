import heapq

def solution(n, works):
    answer = 0
    m = len(works)
    heap = []
    for w in works: # max heap 생성
        heapq.heappush(heap, (-w, w))
    
    for _ in range(n):
        max_work = heapq.heappop(heap)[1]
        if max_work > 0 : 
            max_work -= 1
        heapq.heappush(heap, (-max_work, max_work))
    for w in heap:
        work = w[1]
        answer += work*work
        
    return answer

print(solution(4, [4, 3, 3]), 12)
print(solution(1, [2, 1, 2]), 6)
print(solution(3, [1, 1]), 0)