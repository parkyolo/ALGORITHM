from itertools import permutations
import math

def solution(numbers):
    answer = 0
    numbers_ = []
    
    max_num = 0
    # numbers로 만들 수 있는 모든 경우의 수를 구함
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            if num == 0 or num == 1: continue
            if num in numbers_: continue # 중복 제거
            
            if num > max_num:
                max_num = num
            
            numbers_.append(num)

    # 에라토스테네스의 체
    arr = [True for _ in range(max_num+1)]
    for i in range(2, int(math.sqrt(max_num))+1):
        if arr[i]:
            for j in range(i*2, max_num+1, i):
                arr[j] = False

    # 소수 판별    
    for n in numbers_:
        if arr[n]:
            answer += 1

    return answer

answer = solution("011")
print(answer) #2