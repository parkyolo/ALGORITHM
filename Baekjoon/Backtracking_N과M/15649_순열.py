"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

"""
N, M = map(int, input().split())
v = [0 for _ in range(N+1)]
arr = [0 for _ in range(M)]

def solution(k):
    if k == M:
        print(*arr)
        return
    for i in range(1, N+1):
        if not v[i]:
            v[i] = 1
            arr[k] = i
            solution(k+1)
            v[i] = 0

solution(0)