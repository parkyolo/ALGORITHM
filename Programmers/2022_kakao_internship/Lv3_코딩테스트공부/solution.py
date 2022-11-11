import sys
INF = sys.maxsize
            

def solution(alp, cop, problems):

    target_alp, target_cop = 0, 0

    for problem in problems:
        target_alp = max(target_alp, problem[0])
        target_cop = max(target_cop, problem[1])

    if alp > target_alp: alp = target_alp
    if cop > target_cop: cop = target_cop

    dp = [[INF for _ in range(target_cop+1)] for _ in range(target_alp+1)]  # dp[i][j] : 알고력이 i이고 코딩력이 j인 상태에 도달하는 데 걸리는 최단 시간
    dp[alp][cop] = 0

    for i in range(alp, target_alp+1):
        for j in range(cop, target_cop+1):
            if i+1 <= target_alp: dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)  # 1. 알고력을 높인다.
            if j+1 <= target_cop: dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)  # 2. 코딩력을 높인다.

            for problem in problems:                                        # 3. 문제를 푼다.
                if i < problem[0] or j < problem[1]: continue
                dp[min(i+problem[2], target_alp)][min(j+problem[3], target_cop)] = min(dp[min(i+problem[2], target_alp)][min(j+problem[3], target_cop)], dp[i][j] + problem[4])

    return dp[target_alp][target_cop]

if __name__ == "__main__":
    print(15, solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
    print(13, solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))