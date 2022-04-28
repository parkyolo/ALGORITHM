def sol(dp):
    answer = max(dp)
    n = len(dp)
    dp[1] = max(dp[0], dp[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+ dp[i])
        answer = max(answer, dp[i])
    return answer

def solution(money):
    n = len(money)
    dp = [money[i] for i in range(n)]
    return max(sol(dp[1:]), sol(dp[:-1]))

print(solution([1000, 1, 0, 1, 2, 1000, 0]))
print(solution([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([1,2,3]))