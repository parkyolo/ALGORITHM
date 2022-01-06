def solution(gems):
    answer = []
    min_len = len(gems)+1
    gems_set = set(gems) # 보석 종류
    gems_cnt = {g:0 for g in list(gems_set)} # 포함된 보석 수
    start = 1
    gems = [0] + gems
    n = len(gems)
    for i in range(1, n):
        gems_cnt[gems[i]] += 1
        while gems_cnt[gems[start]] != 1: # 첫번째 보석이 중복되면 시작점을 +=1
            gems_cnt[gems[start]] -= 1
            start += 1
        if 0 not in gems_cnt.values(): # 모든 보석이 포함될 때
            if i-start < min_len:
                min_len = i-start
                answer = [start, i]
            gems_cnt[gems[start]] -= 1
            start += 1
        
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]), [3, 7])
print(solution(["AA", "AB", "AC", "AA", "AC"]), [1, 3])
print(solution(["XYZ", "XYZ", "XYZ"]), [1, 1])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]), [1, 5])