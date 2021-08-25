def notation(n, num):
    t_n = ''
    strs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D','E','F']

    if num == 0:
        return '0'

    while num:
        t_n += strs[num%n]
        num //= n

    return t_n[::-1]

def solution(n, t, m, p):
    answer = ''
    game = ''
    num = 0
    
    while len(answer) < t:
        # n진수로 변환한 숫자를 game 변수에 저장
        game += notation(n, num)
        # 게임 진행
        if len(game) >= m:
            # game 변수에서 p번째 숫자를 answer에 저장
            answer += game[p-1]
            # m명의 차례가 지나갔기 때문에 game 변수를 m명만큼 자름
            game = game[m:]
        num += 1
    
    return answer

print(solution(2,4,2,1),"0111")
print(solution(16,16,2,1),"02468ACE11111111")
print(solution(16,16,2,2),"13579BDF01234567")