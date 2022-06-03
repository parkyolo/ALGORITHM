import sys

def d2n(m, d): # 날짜를 1~365 사이의 숫자로 변환
    days = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    return days[m]+d

N = int(input())
dates = [] # [꽃이 피는 날, 피어있는 마지막 날]
for _ in range(N):
    sm, sd, em, ed = map(int, sys.stdin.readline().split())
    s_date = d2n(sm, sd)
    e_date = d2n(em, ed)-1 # 지는 날보다 하루 전
    dates.append([s_date, e_date])

dates.sort(key=lambda x:-x[1]) # 꽃이 피어있는 마지막 날의 내림차순으로 정렬
answer = 0
start = d2n(3, 1)
end = d2n(11, 30)
while True:
    check = True
    for s_date, e_date in dates:
        if s_date <= start:
            answer += 1
            check = False
            if e_date >= end:
                print(answer)
                exit()
            start = e_date+1
            dates.remove([s_date, e_date])
            break
    if check:
        print(0)
        exit()