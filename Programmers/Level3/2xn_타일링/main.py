def solution(n):
    a = 1
    b = 2
    if n < 3: return n
    for _ in range(3, n+1):
        temp = b
        b = (a + b) % 1000000007
        a = temp
    return b

print(solution(4),5)