"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열

"""

N, M = map(int, input().split())
N_num = list(map(int, input().split()))
N_num.sort()
arr = []

def dfs(k):
    if k == M: return print(*arr)

    for i in range(N):
        if N_num[i] not in arr:
            arr.append(N_num[i])
            dfs(k+1)
            arr.pop()

dfs(0)