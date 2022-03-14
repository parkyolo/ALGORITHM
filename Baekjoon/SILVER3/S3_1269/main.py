a_n, b_n = map(int, input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

a_b = a - b
b_a = b - a
            
print(len(a_b) + len(b_a))