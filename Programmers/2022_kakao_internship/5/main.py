num2loc, max_idx = dict(), 0 # num2loc = {인덱스:위치}

def MakeDict(n, m):
    global num2loc, max_idx

    for i in range(m-1):
        num2loc[max_idx] = (0, i)
        max_idx += 1
    for i in range(n-1):
        num2loc[max_idx] = (i, m-1)
        max_idx += 1
    for i in range(m-1, 0, -1):
        num2loc[max_idx] = (n-1, i)
        max_idx += 1
    for i in range(n-1, 0, -1):
        num2loc[max_idx] = (i, 0)
        max_idx += 1
    max_idx -= 1

def ShiftRow(rc):
    temp = [[] for _ in range(len(rc))]
    for i, row in enumerate(rc):
        if i == len(rc)-1:
            temp[0] = row
            break
        temp[i+1] = row
    return temp

def Rotate(rc):
    global max_idx
    temp = [[c for c in r] for r in rc]
    for idx, loc in num2loc.items():
        x, y = loc
        nx, ny = 0, 0
        if idx < max_idx:
            nx, ny = num2loc[idx+1]
        temp[nx][ny] = rc[x][y]
    return temp

def solution(rc, operations):
    n, m = len(rc), len(rc[0])
    MakeDict(n, m)

    for operation in operations:
        if operation == "Rotate": rc = Rotate(rc)
        else: rc = ShiftRow(rc)
    return rc

print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))