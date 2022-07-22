N, C = map(int, input().split())
X = list(int(input()) for _ in range(N))
X.sort()

start, end = 0, X[-1]
answer = 0

while start <= end:
    mid = (start+end)//2
    cnt = 1
    pre = X[0]
    for i in range(1, N):
        if X[i] - pre >= mid:
            cnt += 1
            pre = X[i]
    
    if cnt >= C:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)