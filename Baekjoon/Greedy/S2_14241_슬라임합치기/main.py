n = int(input())
slime = list(map(int, input().split()))
slime.sort(reverse=True)
ans = 0

for i in range(1,n):
    ans += slime[i-1] * slime[i]
    slime[i] = slime[i-1] + slime[i]
print(ans)