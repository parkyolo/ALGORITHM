def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def isPalindrome(n):
    if str(n) == str(n)[::-1]: return True
    return False

a, b = map(int, input().split())
if b > 10000000: b = 10000000
for num in range(a, b+1):
    if isPalindrome(num):
        if isPrime(num):
            print(num)
print(-1)