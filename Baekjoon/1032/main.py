n = int(input())
cmd = list(input() for i in range(n))
file_length = len(cmd[0])
pattern = cmd[0]

for i in range(file_length):
    w = cmd[0][i]
    for j in range(1, n):
        if cmd[j][i] != w:
            pattern = pattern[:i] + '?' + pattern[i+1:]
            break
print(pattern)