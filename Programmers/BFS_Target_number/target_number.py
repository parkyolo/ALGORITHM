from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])

    while queue:
        v, idx = queue.popleft()
        
        # 모든 원소를 큐에 넣었으면 연산 결과가 target과 같을 때 count
        if idx == len(numbers)-1:
            if v == target:
                answer += 1
        else:
            # 앞의 연산 결과 v와 다음 원소 numbers[idx+1]을 더해서 큐에 넣음
            queue.append([v+numbers[idx+1],idx+1])
            queue.append([v-numbers[idx+1],idx+1])
        
    return answer