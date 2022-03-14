n, l = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()
answer = 0
while hole:
    h = hole.pop()
    answer += 1
    while hole:
        if hole[-1] > h - l:
            hole.pop()
        else:
            break
print(answer)