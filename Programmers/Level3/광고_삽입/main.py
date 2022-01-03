def solution(play_time, adv_time, logs):
    answer = 0
    play_sec = int(play_time[0:2])*60*60 + int(play_time[3:5])*60 + int(play_time[6:8])
    adv_sec = int(adv_time[0:2])*60*60 + int(adv_time[3:5])*60 + int(adv_time[6:8])

    dp = [0 for _ in range(play_sec+1)]
    for log in logs:
        start_log_sec = int(log[0:2])*60*60 + int(log[3:5])*60 + int(log[6:8])
        end_log_sec = int(log[9:11])*60*60 + int(log[12:14])*60 + int(log[15:17])
        dp[start_log_sec] += 1
        dp[end_log_sec] -= 1

    for i in range(1, play_sec+1): # 초당 시청자 수
        dp[i] += dp[i-1]

    for i in range(1, play_sec+1): # 누적 시청자 수
        dp[i] += dp[i-1]
    
    viewers = dp[adv_sec-1] # 00:00:00 ~ adv_time까지의 시청자 수
    for i in range(adv_sec, play_sec):
        if viewers < dp[i] - dp[i-adv_sec]:
            viewers = dp[i] - dp[i-adv_sec]
            answer = i-adv_sec+1

    h = answer // 3600
    m = (answer - h*3600) // 60
    s = answer - h*3600 - m*60
    answer = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    return answer

print(solution("00:01:00", "00:00:03", ["00:00:01-00:00:06", "00:00:04-00:00:45", "00:00:02-00:00:30", "00:00:45-00:01:00"]))
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]), "01:30:59")
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]), "01:00:00")
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]), "00:00:00")