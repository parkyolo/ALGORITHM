a, b = map(int, input().split())
answer = 0 # 언더프라임의 개수

arr = [True for _ in range(b+1)] # 소수는 True
prime = [0 for _ in range(b+1)] # 소인수의 개수

# 에라토스테네스의 체
for i in range(2, b+1):
    if arr[i]:
        prime[i] = 1
        for j in range(i*2, b+1, i):
            arr[j] = False
            cur = j
            # j의 소인수의 개수를 더해줌
            while cur % i == 0:
                cur //= i
                prime[j] += 1

for i in range(a, b+1):
    if arr[i]: continue # i가 소수이면 바로 넘김
    if prime[prime[i]] == 1: answer += 1 # 소인수의 개수가 소수이면 answer += 1

print(answer)