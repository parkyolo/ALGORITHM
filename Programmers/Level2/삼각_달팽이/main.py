def solution(n):
    answer = []

    if n == 1: return [1]
    
    tri = [[0]*(i+1) for i in range(n)]
    num = 1
    # 달팽이 위치
    si = 0
    sj = 0
    # 달팽이가 이동하는 방향 (아래, 오른쪽, 위)
    di = [1,0,-1]
    dj = [0,1,-1]
    # 달팽이가 이동하는 방향의 인덱스
    ds = 0

    while True:
        # 삼각형이 모두 채워지면 while문 종료
        if tri[si][sj] != 0: break
        tri[si][sj] = num
        num += 1
        # 달팽이가 방향을 바꿔야할 때
        if (0 > si + di[ds] or si + di[ds] >= n) or (0 > sj + dj[ds] or sj + dj[ds] >= n) or tri[si+di[ds]][sj+dj[ds]] != 0:
            ds += 1
            ds = ds%3
        # 위치 이동
        si += di[ds]
        sj += dj[ds]

    for c in tri:
        for r in c:
            answer.append(r)
        
    return answer

print(solution(4))
print(solution(5))
print(solution(6))