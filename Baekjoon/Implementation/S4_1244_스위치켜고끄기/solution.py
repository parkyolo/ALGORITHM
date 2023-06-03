import math

n = int(input())     # 스위치 개수
state = list(map(int, input().split())) # 스위치 초기 상태
std_n = int(input()) # 학생 수

def toggleMultiple(num): #  받은 수의 배수인 스위치의 상태를 바꾼다.
    _num = num
    while _num < n+1:
        state[_num-1] = ~state[_num-1] + 2
        _num += num

def toggleArea(num):     # 받은 수를 중심으로 좌우가 대칭이면 스위치의 상태를 바꾼다.
    num -= 1
    s_idx, e_idx = num - 1, num + 1 # 좌우 인덱스
    state[num] = ~state[num] + 2
    while s_idx >= 0 and e_idx < n: # 좌우가 대칭이면 스위치 토글
        if state[s_idx] == state[e_idx]:
            state[s_idx] = ~state[s_idx] + 2
            state[e_idx] = ~state[e_idx] + 2
            s_idx -= 1
            e_idx += 1
        else:                       # 대칭이 아니면 종료
            break
    
for _ in range(std_n):
    flag, num = map(int, input().split())    # 학생의 성별, 받은 수

    if flag == 1:
        toggleMultiple(num)
    else:
        toggleArea(num)

# 한 줄에 20개씩 출력
for i in range(math.ceil(n/20)):
    print(' '.join([str(ele) for ele in state[i*20:min((i+1)*20, n)]]))