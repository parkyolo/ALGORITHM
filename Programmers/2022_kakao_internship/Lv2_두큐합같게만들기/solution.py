from collections import deque

def solution(queue1, queue2):
    answer = 0

    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2) # 두 큐의 합
    length = len(queue1) + len(queue2)

    while sum1 != sum2 and answer < 2*length: # 두 큐의 합이 같거나 모든 원소가 한 번씩 바뀌었으면 종료

        if sum1 > sum2: # sum1이 더 작게 맞춰줌
            sum1, sum2 = sum2, sum1
            queue1, queue2 = queue2, queue1

        num = queue2.popleft()  # queue2에서 pop한 값을
        sum2 -= num
        queue1.append(num)      # queue1에 append
        sum1 += num

        answer += 1

    if sum1 != sum2: # 두 큐의 합을 같게 만들 수 없는 경우 -1을 return
        return -1

    return answer