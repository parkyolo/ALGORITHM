from collections import Counter
def solution(a):
    answer = 0
    n = len(a)
    if n < 2: return 0 # a의 길이가 2보다 작으면 스타 수열을 만들 수 없음

    freq = Counter(a) # a의 원소들의 빈도

    for num, cnt in freq.items(): # num: 원소, cnt: 빈도
        if cnt * 2 <= answer: continue # cnt*2는 해당 원소가 교집합일 때 만들 수 있는 스타 수열의 최대 길이
        v = [0 for _ in range(n)] # a의 원소들이 스타 수열에 포함됐는지 검사
        for idx, val in enumerate(a):
            if val == num and v[idx] == 0: # val가 num일 때 앞 뒤의 원소가 집합에 포함될 수 있는지 검사
                try:
                    if v[idx-1] == 0 and a[idx-1] != num: v[idx-1] = 1
                    elif v[idx+1] == 0 and a[idx+1] != num: v[idx+1] = 1
                    else: continue
                    v[idx] = 1
                except:
                    pass
        if sum(v) > answer: answer = sum(v)
    return answer

print(solution([0]), 0)
print(solution([0, 0, 3, 1, 2, 1, 3, 4, 0, 1, 4]), 6)
print(solution([5, 2, 3, 3, 5, 3]), 4)
print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]), 8) 
print(solution([1, 1, 1, 1, 1, 1, 2, 3, 2, 4]), 4)
print(solution([4, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3]), 6)