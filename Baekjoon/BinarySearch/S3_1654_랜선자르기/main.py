# k, n = 4, 11
# lines = [802, 743, 457, 539]

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))
start = 1
end = max(lines)
mid = end // 2
answer = end
while start <= end:
    if mid == 0: break # ZeroDivisionError가 나서 추가해줌
    cuts = list(map(lambda x: x // mid, lines))
    if sum(cuts) >= n:
        answer = mid
        start, mid = mid + 1, (start + end) // 2
    elif sum(cuts) < n:
        end, mid = mid - 1, (start + end) // 2
print(answer)