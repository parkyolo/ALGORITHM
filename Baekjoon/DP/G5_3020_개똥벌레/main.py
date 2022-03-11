n, h = map(int, input().split())
cave = [0 for _ in range(h)]
for i in range(n):
    hurdle = int(input())
    if i % 2 == 0: # 석순
        cave[0] += 1
        cave[hurdle] -= 1
    else: # 종유석
        cave[h-hurdle] += 1

for i in range(1,h): # 누적합
    cave[i] += cave[i-1]

# print(cave)
min_val = min(cave)
min_cnt = cave.count(min_val)
print(min_val, min_cnt)