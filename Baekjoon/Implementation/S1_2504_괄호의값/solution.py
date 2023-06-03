ps = input() # 입력 괄호열
stack = []

answer = 0

for i in range(len(ps)):
    # 여는 괄호
    if ps[i] == '(' or ps[i] == '[':
        stack.append(ps[i])
    
    # 닫는 괄호
    else:
        
        if len(stack) == 0:
            break
            
        if stack[-1] == '(' and ps[i] == ')':
            stack.pop()
            if stack and stack[-1].isdigit():   # f(xy)인 경우
                stack[-1] = str(int(stack[-1]) + 2)
            else:
                stack.append('2')   # x인 경우
                
        elif stack[-1] == '[' and ps[i] == ']': # f(xy)인 경우
            stack.pop()
            if stack and stack[-1].isdigit():
                stack[-1] = str(int(stack[-1]) + 3)
            else:
                stack.append('3')   # x인 경우
            
        elif ps[i] == ')' and stack[-1].isdigit():
            res = int(stack.pop()) * 2  # f(x)인 경우
            if not stack or stack[-1] != '(':
                break
            stack.pop() # 여는 괄호 제거
            if len(stack) > 0 and stack[-1].isdigit():  # f(xy)인 경우
                res += int(stack.pop())
            stack.append(str(res))
            
            
        elif ps[i] == ']' and stack[-1].isdigit():
            res = int(stack.pop()) * 3  # f(x)인 경우
            if not stack or stack[-1] != '[':
                break
            stack.pop() # 여는 괄호 제거
            if len(stack) > 0 and stack[-1].isdigit():  # f(xy)인 경우
                res += int(stack.pop())
            stack.append(str(res))
        
        else:
            break

if len(stack) == 1 and stack[0].isdigit():
    answer = int(stack[0])
print(answer)