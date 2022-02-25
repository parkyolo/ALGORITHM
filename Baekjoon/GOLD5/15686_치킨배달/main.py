from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []
for r in range(n): # 치킨집과 집의 위치를 배열에 저장
    for c in range(n):
        if city[r][c] == 2:
            chickens.append((r, c))
        elif city[r][c] == 1:
            houses.append((r, c))
combi = list(combinations(chickens, m)) # 치킨집을 m개 선택하는 경우의 수
min_dist = -1
for selected in combi:
    chicken_dist = 0 # 치킨 거리의 합
    for house in houses: # 치킨 거리를 구함
        dist = abs(house[0] - selected[0][0]) + abs(house[1] - selected[0][1])
        for chicken in selected:
            if abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]) < dist:
                dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
        chicken_dist += dist
    if min_dist == -1: min_dist = chicken_dist # 치킨 거리의 합의 최소를 구함
    elif chicken_dist < min_dist: min_dist = chicken_dist

print(min_dist)