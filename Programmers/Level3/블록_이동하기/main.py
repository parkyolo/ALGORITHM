from collections import deque
def solution(board):
    n = len(board)

    # 기존의 board에 패딩을 준 new board
    new_board = [[1 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    rotate = [-1, 1]

    queue = deque()
    v = set()
    queue.append([1,1,1,2,0])
    v.add((1,1,1,2))
    while queue:
        x1,y1,x2,y2,cnt = queue.popleft()

        if (x1 == n and y1 == n) or (x2 == n and y2 == n):
            return cnt
        
        for d in range(4): # 평행이동
            if new_board[x1+dx[d]][y1+dy[d]] == 0 and new_board[x2+dx[d]][y2+dy[d]] == 0:
                if (x1+dx[d], y1+dy[d], x2+dx[d], y2+dy[d]) not in v:
                    queue.append([x1+dx[d], y1+dy[d], x2+dx[d], y2+dy[d], cnt+1])
                    v.add((x1+dx[d], y1+dy[d], x2+dx[d], y2+dy[d]))
        if y1 == y2: # 세로방향일 때 회전
            for d in rotate:
                if new_board[x1][y1+d] == 0 and new_board[x2][y2+d] == 0:
                    if (x1, y1+d, x1, y1) not in v:
                        queue.append([x1, y1+d, x1, y1, cnt+1])
                        v.add((x1, y1+d, x1, y1))
                    if (x2, y2+d, x2, y2) not in v:
                        queue.append([x2, y2+d, x2, y2, cnt+1])
                        v.add((x2, y2+d, x2, y2))
        else: # 가로방향일 때 회전
            for d in rotate:
                if new_board[x1+d][y1] == 0 and new_board[x2+d][y2] == 0:
                    if (x1+d, y1, x1, y1) not in v:
                        queue.append([x1+d, y1, x1, y1, cnt+1])
                        v.add((x1+d, y1, x1, y1))
                    if (x2+d, y2, x2, y2) not in v:
                        queue.append([x2+d, y2, x2, y2, cnt+1])
                        v.add((x2+d, y2, x2, y2))

print(solution(	[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]), 7)