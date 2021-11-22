n = int(input())

for _ in range(n):
    user = input()
    left = []
    right = []
    for u in user:
        if u == "<":
            if len(left) > 0: right.append(left.pop())
        elif u == ">":
            if len(right) > 0: left.append(right.pop())
        elif u == "-":
            if len(left) > 0: left.pop()
        else:
            left.append(u)
    print(''.join(left)+''.join(reversed(right)))