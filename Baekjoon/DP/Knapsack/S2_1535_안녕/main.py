n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [[0 for _ in range(101)] for _ in range(n)]

for i in range(n):
    for j in range(100, 0, -1):
        if j > L[i]:
            # max( i번 사람까지 인사했을 때의 기쁨, i-1번 사람까지 인사했을 때의 기쁨 )
            dp[i][j] = max(dp[i - 1][j - L[i]] + J[i], dp[i - 1][j])
        else:
            # i번 사람과 인사하지 못할 때
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])

"""
1차원 배열로 풀이
체력이 큰 순서대로 기쁨을 sp 배열에 넣어준다.

N = int(input())
strength = list(map(int, input().split()))
pleasure = list(map(int, input().split()))

sp = [[s, p] for s, p in zip(strength, pleasure)]
sp.sort()

hp = [0 for _ in range(100)]
for s, p in sp:
    for j in range(99, s-1, -1):
        hp[j] = max(hp[j-s]+p, hp[j])


print(hp[99])
"""