def solution(n):
    a, b = 0, 1
    for _ in range(n+1):
        a, b = b%1234567, (a+b)%1234567
    return a%1234567

print(solution(4), 5)
print(solution(3), 3)