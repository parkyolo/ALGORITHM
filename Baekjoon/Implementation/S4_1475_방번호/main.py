import math

N = input()
cnt = [0 for _ in range(10)]
ans = 0
for num in N:
    num = int(num)
    cnt[num] += 1
    if num == 6 or num == 9: # 6과 9는 합해서 계산
        ans = max(ans, math.ceil((cnt[6]+cnt[9])/2))
    else:
        ans = max(ans, cnt[num])

print(ans)