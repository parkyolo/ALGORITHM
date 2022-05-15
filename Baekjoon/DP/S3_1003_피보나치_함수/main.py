T = int(input())
cnt = [[1,0], [0,1]]

for _ in range(T):
    N = int(input())
    if N >= len(cnt):
        for i in range(len(cnt), N+1):
            cnt.append([cnt[i-1][0]+cnt[i-2][0], cnt[i-1][1]+cnt[i-2][1]])
    print(" ".join([str(i) for i in cnt[N]]))