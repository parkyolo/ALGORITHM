def is_stable(s):
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        else:
            if stack[-1] == "{" and i == "}":
                stack.pop()
            else:
                stack.append(i)
    
    cnt = 0 # 연산 횟수
    while stack:
        b = stack.pop()
        a = stack.pop()
        cnt += 1
        if a == "}" and b == "{":  # 두 괄호를 다 바꿔야하는 경우
            cnt += 1

    return cnt

def main():
    num = 1
    while True:
        s = input()
        if '-' in s: break
        print("{0}. {1}".format(num, is_stable(s)))
        num += 1
    return

if __name__ == "__main__":
    main()