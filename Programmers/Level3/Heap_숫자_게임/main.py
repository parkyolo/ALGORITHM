import heapq
def solution(A, B):
    answer = 0

    heapq.heapify(A) # 1357
    heapq.heapify(B) # 2268
    while A:
        a = heapq.heappop(A)
        while B:
            b = heapq.heappop(B)
            if b > a:
                answer += 1
                break
            
        
    return answer