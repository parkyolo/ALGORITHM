from collections import deque
def solution(queue1, queue2):
    answer = 0

    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    length = len(queue1) + len(queue2)

    while sum1 != sum2 and answer < 2*length:
        if sum1 > sum2:
            sum1, sum2 = sum2, sum1
            queue1, queue2 = queue2, queue1
        num = queue2.popleft()
        sum2 -= num
        queue1.append(num)
        sum1 += num
        answer += 1

    if sum1 != sum2:
        return -1
    return answer