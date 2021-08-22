def solution(land):
    answer = 0

    for i in range(1, len(land)):
        # 각 행에서의 최적해를 찾음
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][1], land[i-1][2], land[i-1][0])

    answer = max(land[-1])

    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]), 16)