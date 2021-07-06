import heapq

def solution(jobs):
    answer = 0
    
    length = len(jobs) # 마지막에 평균을 구해야하므로 jobs의 길이를 저장해놓음
    jobs.sort() # 먼저 들어온 작업부터 처리해야하므로 sort
    heap = [] # 우선순위 큐를 통해 작업의 순서를 결정
    
    total = 0 # 모든 작업의 [요청부터 종료까지 걸린 시간]을 저장하는 변수
    end_time = 0 # 작업이 끝나는 시간을 저장하는 변수
    
    while jobs: # 이전 작업이 모두 끝난 후에 다음 작업이 시작될 경우를 처리해주기 위해 jobs에 요소가 남아있는지 검사
        heapq.heappush(heap, jobs.pop(0)) # 첫 번째 작업을 힙에 넣음
        end_time = heap[0][0] # 첫 번째 작업의 시작 시간으로 초기화

        while heap:
            work = heapq.heappop(heap) # 현재 작업
            
            # [이전 작업이 끝난 시간] - [작업이 요청된 시점] + [작업의 소요시간] ==> 작업의 요청부터 작업의 시작까지 기다린 시간에 작업의 소요시간을 더해서 [작업의 요청부터 종료까지 걸린 시간]을 구함
            total += end_time - work[0] + work[1]
            end_time += work[1]

            while jobs:
                # 현재 작업을 수행하고 있을 때 들어온 작업들을 큐에 넣음
                if jobs[0][0] <= end_time:
                    heapq.heappush(heap, jobs.pop(0))
                else:
                    break
            
            # 소요시간이 짧은 작업부터 처리해야 하기 때문에 작업의 소요시간을 기준으로 sort
            if heap:
                heap.sort(key=lambda x:x[1])
            
    answer = int(total/length) # 소수점 이하의 수는 버림

    return answer

answer = solution([[0, 5], [2, 10], [100000000000, 2]])
print(answer) #6