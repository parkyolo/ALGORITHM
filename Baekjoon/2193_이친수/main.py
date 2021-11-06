n = int(input())

if n < 2:
    print(1)
    exit()

a, b = 1, 1
for i in range(2, n):
    a, b = b, a+b
print(b)