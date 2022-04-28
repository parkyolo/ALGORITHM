import heapq
def solution(food_times, k):
    answer = -1
    heap = []
    for i, time in enumerate(food_times):
        heapq.heappush(heap, (time, i+1)) # heap : (먹는 시간, 음식 번호)
    previous = 0 # 이전까지 먹은 양
    
    while heap:
        t = (heap[0][0]-previous)*len(heap) # 현재 먹는데 걸리는 시간 = 섭취 시간이 가장 적게 남은 음식을 다 먹는데 걸리는 시간 * 남은 음식 개수
        if k >= t: # 다 먹을 수 있다면
            k -= t
            previous = heap[0][0]
            heapq.heappop(heap)
        else: # 다 먹을 수 없다면
            heap.sort(key=lambda x:x[1])
            idx = k%len(heap) # 몇 번 음식까지 먹었는지 구하기
            answer = heap[idx][1]
            break
            
    return answer


print(solution([3,1,2], 5), 1)
print(solution([4,2,3,6,7,1,5,8], 16), 3)