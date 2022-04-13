from sys import stdin

s_left = list(input())
s_right = []
n = int(input())
for i in range(n):
    cmd = stdin.readline().strip().split()
    if cmd[0] == 'L' and len(s_left) > 0:
        s_right.append(s_left.pop())
    elif cmd[0] == 'D' and len(s_right) > 0:
        s_left.append(s_right.pop())
    elif cmd[0] == 'B' and len(s_left) > 0:
        s_left.pop()
    elif cmd[0] == 'P':
        s_left.append(cmd[1])
answer = ""
for l in s_left:
    answer += l
while s_right:
    answer += s_right.pop()
print(answer)