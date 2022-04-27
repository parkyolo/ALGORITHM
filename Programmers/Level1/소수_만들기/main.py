from itertools import combinations
def solution(nums):
    answer = 0
            
    combi = list(combinations(nums, 3)) # 원소가 3개인 조합 구하기
    for c in combi:
        sum_ = sum(c)
        check = True
        for i in range(2, sum_): # 소수 판별
            if sum_%i == 0: check = False; break;
        if check: answer += 1 # 소수이면 answer += 1
        
    return answer