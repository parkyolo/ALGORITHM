import re

n = int(input())
numbers = []
for i in range(n):
    numbers.append(input())

numbers.sort(key=lambda x: (len(x), sum(map(int,list(''.join(re.findall("\d+",x))))), x))
for n in numbers:
    print(n)