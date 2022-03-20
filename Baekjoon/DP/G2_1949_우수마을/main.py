import sys
sys.setrecursionlimit(10**6)

n = int(input())
population = list(map(int, input().split()))
tree = {i:[] for i in range(n)}
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
dp = [[0 for _ in range(2)] for _ in range(n)]
v = [0 for _ in range(n)]

def dfs(cur):
    v[cur] = 1
    dp[cur][0] = 0 # 일반 마을일 때 초기값
    dp[cur][1] = population[cur] # 우수 마을일 때 초기값

    for next in tree[cur]:
        if v[next]: continue
        dfs(next) # 자식 노드에도 초기값 세팅

        dp[cur][0] += max(dp[next][0], dp[next][1]) # 일반 마을일 때 자식 노드가 일반 마을일 수도 있고 우수 마을일 수도 있음
        dp[cur][1] += dp[next][0] # 우수 마을일 때 자식 노드는 일반 마을

dfs(0)
print(max(dp[0][0], dp[0][1]))