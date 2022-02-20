s = input()
stack = []
length = 0
for i, s_ in enumerate(s):
    if s_.isdigit():
        length += 1
    elif s_ == "(":
        stack.append((int(s[i-1]), length-1)) 
        length = 0
    else:
        pre_num, num_cnt = stack.pop() # K, 괄호 이전까지의 문자열의 개수
        length = (pre_num * length) + num_cnt # K*Q + 이전 문자열의 개수

print(length)