def solution(distance, rocks, n):
    rocks.sort()
    start = 0
    end = distance # [2, 11, 14, 17, 21]
    while start <= end:
        mid = (start+end)//2 # 바위 사이의 거리의 최솟값
        cnt, pre = 0, 0 # 제거한 바위의 개수, 제거하지 않은 바로 이전의 바위
        for rock in rocks: # 바위 사의의 거리가 mid보다 작으면 바위를 제거
            if rock-pre < mid: 
                cnt += 1
            else: pre = rock
        if distance-pre < mid:
            cnt += 1
        
        if cnt > n: # 제거한 바위가 n보다 많으면 작은 범위 탐색
            end = mid-1
        else:
            start = mid+1
    return end

print(solution(34, [5, 19, 28], 2), 15)
print(solution(25, [2,14,11,21,17],2), 4)