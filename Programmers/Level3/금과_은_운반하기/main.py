def solution(a, b, g, s, w, t):
    
    n = len(g)
    max_time = sum([(a//w[i]+1)*t[i]*2 + (b//w[i]+1)*t[i]*2 for i in range(n)])
    answer = max_time
    start = 0; end = max_time
    while start <= end:
        mid = (start + end) // 2
        total_g = 0; total_s = 0; total = 0;
        for i in range(n):
            move_cnt = mid // (t[i] * 2) # mid시간동안 이동할 수 있는 횟수
            if mid % (t[i] * 2) >= t[i]: move_cnt += 1

            total_g += g[i] if move_cnt * w[i] >= g[i] else move_cnt * w[i]
            total_s += s[i] if move_cnt * w[i] >= s[i] else move_cnt * w[i]
            total += g[i] + s[i] if move_cnt * w[i] >= g[i] + s[i] else move_cnt * w[i]

        if total_g >= a and total_s >= b and total >= a+b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer

print(solution(10, 10, [100], [100], [7], [10]), 50)
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]), 499)