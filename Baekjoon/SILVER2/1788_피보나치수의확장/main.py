n = int(input())
m = abs(n)

ans = 0
if m == 0: ans = 0
else:
    a, b = 0, 1
    for i in range(2, m+1):
        b, a = (a+b)%1000000000, b%1000000000
    ans = b % 1000000000

if n < 0 and n%2 == 0: print(-1)
elif n == 0: print(0)
else: print(1)
print(ans)