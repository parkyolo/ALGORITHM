n = int(input())
asg = [list(map(int, input().split())) for _ in range(n)]
asg.sort(key=lambda x:(-x[0], -x[1])) # 마감일이 늦고 점수가 높은 순으로 정렬
time = asg[0][0] # 가장 늦은 마감일
score = [0 for _ in range(time+1)] # i일 남은 과제 중 최대 스코어 score[i]

for t in range(time, 0, -1):
    max_score, idx = 0, -1
    for i, a in enumerate(asg):
        if a[0] >= t and a[1] > max_score: # 마감일이 t일 이상 남은 과제 중 가장 점수가 높은 과제를 선택
            max_score = a[1]; idx = i
        elif a[0] < t:
            break
    score[t] = max_score
    if idx != -1: asg[idx][1] = -1 # 이미 과제를 끝냈다면 점수를 -1로 변경

print(sum(score[1:]))