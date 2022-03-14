n = int(input())
arr = list(map(int, input().split()))

for i, a in enumerate(arr): # 입력 순서대로 index 추가
    arr[i] = [a, i]

arr.sort(key=lambda x: x[0]) #  입력 좌표의 오름차순으로 정렬

idx = 0
temp = arr[0][0]
for a in arr: # 오름차순 정렬된 index 추가
    if a[0] == temp: a.append(idx)
    elif a[0] > temp:
        idx += 1
        temp = a[0]
        a.append(idx)

arr.sort(key=lambda x:x[1]) # 입력 index로 정렬
ans = [str(a[2]) for a in arr] # 정렬 index 배열에 담기
print(" ".join(ans))