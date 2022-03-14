che = [-1 for _ in range(246913)]

while True:
    n = int(input())
    if n == 0: break
    for i in range(2, 2*n+1):
        if che[i] == -1: 
            che[i] = 1
            for j in range(2, 246912//i+1):
                if che[i*j] == -1: che[i*j] = 0
    cnt = 0
    for i in range(n+1, 2*n+1):
        if che[i] == 1: 
            cnt += 1
    print(cnt)