from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        temp = [] # 각 course의 가능한 메뉴 조합을 저장하는 변수
        for o in orders:
            combi = combinations(sorted(o), c) # 각 주문에서 구성할 수 있는 메뉴 조합
            temp += combi
        cnt = Counter(temp) # 조합들의 개수를 카운트
        if len(cnt) > 0 and max(cnt.values()) > 1: # 조합의 수가 0보다 크고 2명 이상의 손님이 주문했을 경우
            answer += [''.join(i) for i in cnt if cnt[i] == max(cnt.values())]
    return sorted(answer)

answer = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
print(answer)