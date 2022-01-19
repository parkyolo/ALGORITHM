def solution(n, times):
    answer = 0
    times.sort()
    start = 0
    end = times[-1] * n

    while start <= end:
        mid = (start+end) // 2
        total = 0
        for time in times:
            total += mid // time
            if total >= n: break

        if total >= n: 
            answer = mid
            end = mid - 1
        else: start = mid + 1

    return answer

print(solution(6, [7,10]), 28)