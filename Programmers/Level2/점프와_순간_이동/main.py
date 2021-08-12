def solution(n):
    ans = 0
    
    while n:
        if n%2 == 1:
            n -= 1
            ans += 1
        else:
            n /= 2
            
    return ans

print(solution(2), 1)
print(solution(5), 2)
print(solution(6), 2)
print(solution(5000), 5)