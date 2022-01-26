def dec_to_k(n, k): # 10진법 -> k진법
    k_n = ""
    while n:
        k_n = str(n%k) + k_n
        n //= k
    return k_n

def isprime(n): # 소수 판별
    if n == 1: return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0 : return False
    return True

def solution(n, k):
    answer = 0
    k_n = dec_to_k(n, k)

    non_0 = k_n.split("0")
    for s in non_0:
        if s and isprime(int(s)): answer += 1
        
    return answer

print(solution(437674, 3), 3)
print(solution(110011, 10), 2)
print(solution(11, 10), 1)