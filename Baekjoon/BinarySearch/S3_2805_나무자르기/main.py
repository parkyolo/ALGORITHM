n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = 2000000000 # 높이의 최댓값
mid = (start+end)//2
while start < mid:
    total = sum([t - mid if t > mid else 0 for t in trees])
    if total >= m:
        start = mid
        mid = (start+end)//2
    else:
        end = mid
        mid = (start+end)//2
print(mid)