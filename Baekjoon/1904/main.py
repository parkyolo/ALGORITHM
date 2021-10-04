n = int(input())
a = 0
b = 1
for i in range(n):
    a, b = b, a+b
    a %= 15746
    b %= 15746
print(b)

"""
시간 초과

from itertools import permutations
answer = 0
n = int(input())
for i in range(n//2+1):
    temp = []
    for _ in range(i): temp.append('00')
    for _ in range(n-2*i): temp.append('1')
    answer += len(set(permutations(temp,n-i)))
    answer %= 15746
print(answer)
"""