def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 위에서부터 더했을 때 큰 수를 선택하면서 내려옴
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    # 가장 마지막 줄에서 가장 큰 수를 선택
    answer = max(triangle[len(triangle)-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]),30)