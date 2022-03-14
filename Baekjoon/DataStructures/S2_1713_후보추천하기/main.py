n = int(input())
n_recommend = int(input())
candi = list(map(int, input().split()))
board = {}
for c in candi:
    if c in board:
        board[c] += 1
    else:
        if len(board) == n:
            min_candi = [k for k, v in board.items() if min(board.values()) == v]
            board.pop(min_candi[0])
        board[c] = 1

result = list(board.keys())
result.sort()
result = [str(r) for r in result]
print(' '.join(result))