import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)

        # scoville score of mixed foods
        new_scoville = first_min + second_min * 2
        heapq.heappush(scoville, new_scoville)
        answer += 1
        
        # case of -1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
answer = solution(scoville, K)
print(answer) # 2
