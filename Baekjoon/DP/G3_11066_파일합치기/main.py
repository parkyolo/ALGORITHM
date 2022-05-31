N = int(input())
min_arr = list(map(int, input().split()))
max_arr = [i for i in min_arr]
for _ in range(N-1):
    arr = list(map(int, input().split()))
    min_arr = [arr[0]+min(min_arr[0], min_arr[1]), arr[1]+min(min_arr), arr[2]+min(min_arr[1], min_arr[2])]
    max_arr = [arr[0]+max(max_arr[0], max_arr[1]), arr[1]+max(max_arr), arr[2]+max(max_arr[1], max_arr[2])]

print(max(max_arr), min(min_arr))