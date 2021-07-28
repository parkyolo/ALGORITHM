def check(s):
    stack = []
    left = ["[", "(", "{"]
    right = ["]", ")", "}"]
    stack.append(s[0])

    # 올바른 괄호인지 확인
    for i in range(1, len(s)):
        if stack:
            if stack[-1] in left and s[i] in right:
                if left.index(stack[-1]) == right.index(s[i]):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    # 올바른 괄호이면 True 리턴
    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0

    for i in range(len(s)):
        if check(s):
            answer += 1
        # s 회전
        s = s[1:] + s[:1]

    return answer

print(solution("[](){}"), 3)
print(solution("}]()[{"), 2)
print(solution("[)(]"), 0)
print(solution("}}}"), 0)