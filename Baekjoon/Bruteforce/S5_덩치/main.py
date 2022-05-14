n = int(input())
people = list(list(map(int, input().split())) for _ in range(n))
score = [1 for _ in range(n)]
for i, info in enumerate(people):
    x1, y1 = info
    for x2, y2 in people:
        if x1 < x2 and y1 < y2:
            score[i] += 1

for s in score:
    print(s, end=' ')