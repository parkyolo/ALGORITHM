ex = input()
num = ''
operands = []
operators = []
# 연산자와 피연산자를 배열에 넣음
for e in ex:
    if e == '-' or e == '+':
        operands.append(int(num))
        operators.append(e)
        num = ''
    else:
        num += e
operands.append(int(num))

answer = 0
plusnum = 0 # 더해진 수
check = 0
for idx, operand in enumerate(operands):
    if idx == 0:
        plusnum += operand
    else:
        if operators[idx-1] == '+': # '+' 연산
            plusnum += operand
        else: # '-' 연산
            if check == 0: # 처음 '-'가 나왔을 때는 지금까지 더해진 수를 answer에 더해줌
                answer += plusnum
                check = 1
            else: # 더해진 수를 앞의 피연산자에 빼줌
                answer -= plusnum
            plusnum = operand
if check == 0:
    answer += plusnum
else:
    answer -= plusnum
print(answer)