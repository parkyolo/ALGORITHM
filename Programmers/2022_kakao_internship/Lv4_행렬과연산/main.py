from collections import deque
n, m = 0, 0
first_col, last_col, rows = [], [], []


def Rotate():
    rows[0].appendleft(first_col.popleft())
    last_col.appendleft(rows[0].pop())
    rows[n-1].append(last_col.pop())
    first_col.append(rows[n-1].popleft())


def ShiftRow():
    first_col.appendleft(first_col.pop())
    rows.appendleft(rows.pop())
    last_col.appendleft(last_col.pop())


def solution(rc, operations):
    global n, m, first_col, last_col, rows

    n, m = len(rc), len(rc[0])
    # 1번째 열과 마지막 열, 이를 제외한 행들을 따로 저장
    first_col = deque([rc[i][0] for i in range(n)])
    last_col = deque([rc[i][m-1] for i in range(n)])
    rows = deque([deque([rc[i][j] for j in range(1, m-1)]) for i in range(n)])

    for operation in operations:
        if operation == "Rotate": Rotate()
        else: ShiftRow()

    for i in range(n):
        rc[i] = list(rows.popleft())
        rc[i] = [first_col.popleft()] + rc[i]
        rc[i] += [last_col.popleft()]

    return rc


if __name__ == "__main__":
    print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
    print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))  