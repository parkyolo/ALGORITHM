from collections import deque

def solution(m, n, puddles):
    answer = 0
    
    road = [[0]*(m+1) for _ in range(n+1)]
    road[1][1] = 1 # 출발점
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            # 웅덩이가 있는 자리는 0을 넣음
            if [j, i] in puddles:
                road[i][j] = 0
            # [i,j]에 도착하는 경우의 수는 [i-1, j] + [i, j-1]
            else:
                road[i][j] = road[i-1][j] + road[i][j-1]

    answer = road[n][m]
    return answer % 1000000007

print(solution(4, 3, [[2,2]]))
print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(100, 100, []), 690285631)