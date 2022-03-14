n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dic = {key:val for val, key in enumerate(b)}
arr = [] # a의 원소들의 b에서의 index
for i in a:
    arr.append(dic[i])

def binarySearch(lis, target, start, end):
    while start < end:
        mid = (start+end) // 2
        if target > lis[mid]: start = mid+1
        else: end = mid
    return end

lis = [arr[0]] # b에서 증가하는 인덱스로 존재하는 a의 원소들의 부분 수열
for j in range(1, n):
    if arr[j] > lis[-1]: lis.append(arr[j])
    else:
        idx = binarySearch(lis, arr[j], 0, len(lis)-1)
        lis[idx] = arr[j]
        
print(len(lis))