def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        else: # ')'일 때
            if len(stack) > 0: # stack에 값이 있으면 올바른 괄호
                stack.pop()
            else: # stack에 값이 없으면 짝이 안맞으므로 return False
                return False
    
    # 모든 문자열을 탐색했는데 stack에 값이 남아있다면 짝이 맞지 않는 것이므로 return False
    if len(stack) > 0: return False
    else: return True

print(solution("()()"),True)
print(solution("(())()"),True)
print(solution(")()("),False)
print(solution("(()("),False)