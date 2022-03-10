n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)-min(arr)

def canDivideintoM(target): # (구간의 최댓값-최솟값)의 최댓값이 target일 때, m개의 구간으로 나눌 수 있는지
    min_val, max_val = arr[0], arr[0]
    cnt = 1 # 구간의 수
    for i in range(1, n):
        min_val = min(arr[i], min_val)
        max_val = max(arr[i], max_val)
        if (max_val-min_val) > target: # (최댓값-최솟값)의 최댓값이 target이어야 하므로, target보다 크면 다음 구간으로 넘김
            cnt += 1
            if cnt > m: return False # 구간이 m개보다 많아지면 안됨
            min_val, max_val = arr[i], arr[i]
    return True

while start < end:
    mid = (start+end) // 2
    if canDivideintoM(mid): end = mid # mid가 (최댓값-최솟값)의 최댓값이 될 수 있을 때, mid보다 작은 범위를 탐색
    else: start = mid+1 # mid로 m개 이하의 구간을 나눌 수 없을 때, mid보다 큰 범위를 탐색

print(end)