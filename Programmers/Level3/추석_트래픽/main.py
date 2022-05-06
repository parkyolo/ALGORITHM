def solution(lines):
    answer = 0
    times = []
    
    for line in lines:
        _, s, t = line.split()
        h, m, sec = map(float, s.split(":"))
        t = round(float(t[:-1]), 3) - 0.001

        end_sec = round(h*3600+m*60+sec, 3)
        start_sec = round(end_sec - t, 3)

        times.append((start_sec, end_sec))
    
    times.sort(key=lambda x:x[1]) # 끝 시간을 기준으로 정렬

    for i, time in enumerate(times):
        cnt = 0
        for j in range(i, len(times)):
            next_time = times[j]            
            if next_time[0] < time[1]+1: # i보다 늦게 끝나는 로그 중 (i의 끝 시간 + 1초) 전에 시작하는 로그
                cnt += 1
        answer = max(answer, cnt)

    return answer

print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]), 2)
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]), 7)