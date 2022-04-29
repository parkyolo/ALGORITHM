n, k = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(n)]
things = [[0,0]]+things
things.sort() # 무게 순으로 정렬

knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1): # i : 배낭에 넣을 물건의 index (1~n)
    for j in range(1, k+1): # j : 배낭에 넣을 수 있는 물건의 무게
        if j >= things[i][0]: # i번째 물건이 배낭에 들어갈 수 있을 경우
            # i번째 물건인 things[i]를 넣는 경우 --> things[i]의 가치 + 이전 배낭에서 j-things[i]의 무게만큼 덜 넣었을 때의 가치
            # 안넣는 경우 --> 이전 배낭인 knapsack[i-1]에 j만큼의 무게를 넣었을 때의 가치인 knapsack[i-1][j]
            # 둘 중 큰 값으로 갱신
            knapsack[i][j] = max(things[i][1]+knapsack[i-1][j-things[i][0]], knapsack[i-1][j])
        else:
            knapsack[i][j] = knapsack[i-1][j]
print(knapsack[-1][-1])


"""
1차원 배열을 이용한 풀이
물건이 하나씩만 있을 때에는 큰 배낭부터(무게가 K일 때부터) 넣어준다.

knapsack = [0 for _ in range(K+1)]
for w, v in things:
    for j in range(K, w-1, -1):
        knapsack[j] = max(knapsack[j-w]+v, knapsack[j])
print(knapsack[K])

"""