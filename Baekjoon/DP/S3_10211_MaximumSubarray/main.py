t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    #arr.reverse()
    cur_sum = 0
    max_sum = arr[0]
    for a in arr:
        cur_sum = max(cur_sum+a, a)
        max_sum = max(max_sum, cur_sum)
    print(max_sum)