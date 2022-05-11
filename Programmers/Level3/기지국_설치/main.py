import math
def solution(n, stations, w):
    answer = 0

    start = 1 # 이전 기지국의 전파가 도달하지 않은 위치
    left, right = 0, 0
    for station in stations:
        left, right = station-w-1, station+w+1 # 기지국의 전파가 도달하지 않는 범위
        if start <= left:
            answer += math.ceil((left-start+1)/(2*w+1)) # 기지국을 하나 세우면 (2*w+1)만큼 전파를 전달할 수 있음
        start = right

    if start <= n: # 마지막 기지국의 오른쪽 남은 범위
        answer += math.ceil((n-start+1)/(2*w+1))
        
    return answer