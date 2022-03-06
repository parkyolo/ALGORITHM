n = int(input())
wire = list(map(int, input().split()))
lis = []

def bs(n,start,end):
    while start < end:
        mid = (start+end)//2
        if n <= lis[mid]: end = mid
        else: start = mid+1
    return end

lis.append(wire[0])
for i in range(1,n):
    if wire[i] > lis[-1]: lis.append(wire[i])
    else:
        idx = bs(wire[i],0,len(lis)-1)
        lis[idx] = wire[i]

print(n-len(lis))

# dp 풀이
# dp = [0 for _ in range(n)]
# for i in range(n):
#     dp[i] = 1
#     for j in range(i):
#         if wire[j] < wire[i]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(n-max(dp))