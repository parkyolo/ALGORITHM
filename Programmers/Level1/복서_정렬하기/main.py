def solution(weights, head2head):
    answer = []
    info = []

    for i,h in enumerate(head2head):
        boxer = [i+1, 0, 0, weights[i]] # 번호, 승률, 자신보다 몸무게가 무거운 복서를 이긴 횟수, 몸무게
        win = lose = 0
        for j, w in enumerate(h):
            if w == 'W':
                win += 1
                if weights[i] < weights[j]: # 자신보다 몸무게가 무거운 복서를 이긴 횟수
                    boxer[2] += 1
            elif w == 'L':
                lose += 1
        # 승률
        if win == 0: boxer[1] = 0
        else: boxer[1] = (win / (win + lose))*100
        info.append(boxer)

    # 4가지 조건으로 정렬
    info.sort(key = lambda x : (-x[1], -x[2], -x[3], x[0]))
    
    for s in info:
        answer.append(s[0])

    return answer

print(solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]),[3,4,1,2])
print(solution([145,92,86],["NLW","WNL","LWN"]),[2,3,1])
print(solution([60,70,60],["NNN","NNN","NNN"]),[2,1,3])