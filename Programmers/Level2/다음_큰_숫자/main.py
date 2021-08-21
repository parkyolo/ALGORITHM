def solution(n):
    # n의 1의 갯수
    cnt_n = bin(n)[2:].count('1')
    answer = n+1
    # n보다 큰 수들의 1의 갯수를 세면서 cnt_n과 같아지면 return
    while True:
        cnt_a = bin(answer)[2:].count('1')
        if cnt_a == cnt_n:
            return answer
        answer += 1

print(solution(78), 83)
print(solution(15),23)