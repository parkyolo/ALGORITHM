import math
def solution(enroll, referral, seller, amount):
    answer = []
    graph = {}
    for e, r in zip(enroll, referral):
        graph[e] = [r, 0] # [추천인, 이익금]

    for s, a in zip(seller, amount):
        who = s # 이익금을 받을 사람
        a = a*100 # 순수 이익금
        while a:
            if who == '-': break
            give = math.floor(a/10) # 추천인에게 줄 이익금
            graph[who][1] += a - give # 추천인에게 줄 이익금을 제외한 이익금
            who = graph[who][0] # 추천인
            a = give
    
    for e in enroll:
        answer.append(graph[e][1])

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]), [360, 958, 108, 0, 450, 18, 180, 1080])
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]), 	[0, 110, 378, 180, 270, 450, 0, 0])