from itertools import permutations

def solution(expression):
    answer = 0

    oper = [] # 연산자 종류를 저장
    operator = [] # 연산자를 순서대로 저장
    operand = [] # 피연산자를 순서대로 저장
    s = '' # 하나의 피연산자를 저장하는 변수

    # expression의 연산자와 피연산자를 각 배열에 넣어줌
    for o in expression:
        if o == "+" or o == "-" or o == "*":
            if o not in oper:
                oper.append(o)
            operator.append(o)
            operand.append(int(s))
            s = ''
        else:
            s += o
    operand.append(int(s))

    # 연산자 우선순위의 경우의 수를 생성
    permu = list(permutations(oper, len(oper)))

    # 우선순위의 모든 경우의 수를 계산
    for p in permu:
        idx = 0 # 연산자의 index
        c_operator = operator[:] # operator 배열 복사
        c_operand = operand[:] # operand 배열 복사

        while c_operator:
            o = p[idx] # 우선순위가 높은 연산자부터 o에 값을 넣어줌
            
            for i in range(len(c_operator)):
                # 해당 우선순위의 연산자와 같은 연산자일 때
                # 연산을 수행하고
                # 연산 결과를 피연산자의 자리에 다시 넣어주고
                # 연산된 연산자와 피연산자는 슬라이싱을 통해 삭제
                if c_operator[i] == o:
                    if o == "+":
                        c_operand[i] = c_operand[i] + c_operand[i+1]
                        c_operand = c_operand[:i+1] + c_operand[i+2:]
                    elif o == "-":
                        c_operand[i] = c_operand[i] - c_operand[i+1]
                        c_operand = c_operand[:i+1] + c_operand[i+2:]
                    elif o == "*":
                        c_operand[i] = c_operand[i] * c_operand[i+1]
                        c_operand = c_operand[:i+1] + c_operand[i+2:]
                    c_operator = c_operator[:i] + c_operator[i+1:]
                    break
                # 더 이상 해당 연산자가 없을 경우
                # 다음 우선순위인 연산자로 넘어감
                elif i == len(c_operator)-1:
                    idx += 1
                    break

        # 연산결과의 절댓값의 최댓값을 answer에 저장
        if abs(c_operand[0]) > answer:
            answer = abs(c_operand[0])
            
    return answer

print(solution("100-200*300-500+20"), 60420)
print(solution("50*6-3*2"), 300)