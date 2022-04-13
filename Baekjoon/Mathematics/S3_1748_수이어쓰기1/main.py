n = int(input())
answer = 0
a = len(str(n))
while n:
    answer += (n - 10**(a-1) + 1) * a
    a -= 1
    n = 10**a -1
print(answer)