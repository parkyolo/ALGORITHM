n = int(input())
weight = list(map(int, input().split()))
weight.sort()
target = 1
for i in range(n):
    if target >= weight[i]:
        target += weight[i]
    else:
        break
print(target)