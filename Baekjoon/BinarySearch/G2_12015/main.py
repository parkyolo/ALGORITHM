N = int(input())
a = list(map(int, input().split())) # 수열 A
ans = [a[0]]

def binary_search(start, end, target):
    while start < end:
        mid = (start + end) // 2
        if ans[mid] < target: # 수열의 값이 target보다 작으면 더 큰 범위 탐색
            start = mid+1 # target보다 작은 값의 다음 자리에 target이 들어감
        else:
            end = mid # 더 작은 범위에 target보다 작은 값이 있는지 탐색
    return start

for i in range(1, N):
    if a[i] > ans[-1]:
        ans.append(a[i])
    else:
        idx = binary_search(0, len(ans)-1, a[i]) # a[i]가 들어갈 수 있는 idx 찾기
        ans[idx] = a[i]

# print(ans)
print(len(ans))