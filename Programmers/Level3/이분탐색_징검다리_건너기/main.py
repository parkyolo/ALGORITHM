def solution(stones, k):
    start = min(stones)
    end = max(stones)

    while start + 1 < end:
        mid = (start+end)//2 # 니니즈 수
        dist = 0 # 건널 수 있는 디딤돌 사이의 거리
        for stone in stones:
            if stone < mid:
                dist += 1
                if dist >= k: break # 디딤돌 사이의 거리가 k보다 크면 건널 수 없음
            else:
                dist = 0
        
        if dist >= k:
            end = mid
        else:
            start = mid
            
    return start

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3), 3)