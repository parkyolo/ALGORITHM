def str_to_time(time):
    return int(time[:2]) * 60 + int(time[3:])

def time_to_str(time):
    return "%02d:%02d"%(time // 60, time % 60)

def solution(n, t, m, timetable):
    # 9시는 540분
    # 540 + t * i (0 <= i < n)에 버스가 도착
    # 도착 시각 <= 540 + t * i인 크루가 m명까지 탈 수 있음
    timetable = [str_to_time(time) for time in timetable]
    timetable.sort()
    index, cnt, arrival_time = 0, 0, 0
    for i in range(n):
        arrival_time = 540 + t * i # 셔틀버스 도착 시간
        cnt = 0 # 현재 몇 명이 탔는지
        while timetable[index] <= arrival_time and cnt < m:
            cnt += 1
            index += 1
            if index >= len(timetable): break

    result_time = 0 # 콘의 도착시간
    if cnt < m: # 자리가 남아있으면
        result_time = arrival_time
    else: # 자리가 없으면 마지막으로 탄 사람보다 1분 먼저 도착
        result_time = timetable[index-1]-1

    answer = time_to_str(result_time)
    return answer

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]), "09:00")
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]), "09:09")
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]), 	"08:59")
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]), "00:00")
print(solution(1, 1, 1, ["23:59"]), "09:00")
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]), "18:00")