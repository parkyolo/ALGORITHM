N, K = map(int, input().split())
scores = list(map(int, input().split()))

answer = 0
start, end = 0, sum(scores)+1
while start+1 < end:
    mid = (start + end) // 2 # 점수 합의 최솟값 중 최대인 값
    cnt = 0
    target = mid
    for i in range(N):
        target -= scores[i]
        if target <= 0: # 점수의 합이 target보다 커지면 그룹을 나눔
            cnt += 1
            target = mid

    if cnt < K: # 그룹의 수가 K보다 작으면 기준 점수를 낮춰서 그룹의 수가 더 많아지게 함
        end = mid
    else: # K보다 크거나 같으면 기준 점수를 높여서 그룹의 수가 더 적어지게 함
        start = mid

print(start)