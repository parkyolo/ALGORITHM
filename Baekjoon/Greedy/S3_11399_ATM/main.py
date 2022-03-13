n = int(input())
time = list(map(int, input().split()))
time.sort()
total = 0
pre_sum = 0
for t in time:
    pre_sum += t
    total += pre_sum
print(total)