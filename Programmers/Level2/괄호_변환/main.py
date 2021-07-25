def recur(p):
    answer = ''

    left = 0
    right = 0
    idx = 0

    if p == "":
        return ""

    for i in range(len(p)):
        # 괄호의 개수를 count
        if p[i] == "(":
            left += 1
        else:
            right += 1
        # 균형잡힌 괄호 문자열이 되면 해당 인덱스를 idx 변수에 저장하고 break
        if left == right:
            idx = i #1
            break

    queue = []
    u = p[:idx+1] # 균형잡힌 괄호 문자열 u
    v = p[idx+1:]

    # u가 올바른 괄호 문자열인지 검사
    for i in range(idx+1):
        if queue:
            if queue[-1] == "(" and u[i] == ")":
                queue.pop()
            else:
                queue.append(u[i])
        else:
            queue.append(u[i])

    emp = ''
    # u가 올바른 괄호 문자열이면 answer에 더해줌
    if len(queue) == 0:
        answer += u
    # u가 올바른 괄호 문자열이 아니면 4번의 과정 수행
    else:
        emp += "("
        emp += recur(v)
        v = ""
        emp += ")"
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == "(":
                emp += ")"
            else:
                emp += "("
    answer += emp

    # v가 빈 문자열이 아니면 v에 대해 재귀함수 실행
    if len(v) != 0:
        answer += recur(v)

    return answer

def solution(p): 
    answer = recur(p)
    return answer

print(solution("()))((()"), "()(())()")