def solution(n):
    # 자기자신은 무조건 포함
    answer = 1
    
    start_num = 1
    while start_num < n:
        s_num = 0 # 연속된 자연수의 합
        now = start_num
        while s_num < n: # 연속된 자연수의 합이 n보다 커지면 종료
            s_num += now
            now += 1
        if s_num == n: # 연속된 자연수의 합이 n과 같으면 answer += 1
            answer += 1
        start_num += 1

    return answer

print(solution(15), 4)