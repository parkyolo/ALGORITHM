"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

"""

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []

def dfs(k):
    if len(arr) == M: return print(*arr)

    for i in range(k, N):
        if nums[i] not in arr:
            arr.append(nums[i])
            dfs(i+1)
            arr.pop()

dfs(0)