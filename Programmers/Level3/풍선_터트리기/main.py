def solution(a):
    answer = len(a)

    cnt = [0 for _ in range(len(a))]
    min_val = a[0]
    for i in range(len(a)):
        if min_val < a[i]:
            cnt[i] += 1
        min_val = min(min_val, a[i])
    
    min_val = a[-1]
    for i in range(len(a)-2, 0, -1):
        if min_val < a[i] and cnt[i] == 1:
            answer -= 1
        min_val = min(min_val, a[i])
            
    return answer

print(solution([9, -1, -5]), 3)
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]), 6)