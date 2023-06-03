n = int(input())    # 색종이 수
board = [[0 for _ in range(100)] for _ in range(100)]

def attach(y, x):
    for j in range(y, y+10):
        for i in range(x, x+10):
            board[j][i] = 1

for _ in range(n):
    y, x = map(int, input().split())
    attach(y, x)

cnt = 0
for j in range(100):
    for i in range(100):
        if board[j][i] == 1:
            cnt += 1

print(cnt)