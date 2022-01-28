from collections import deque
import sys
 
def solution(board):
    answer = sys.maxsize
    n = len(board)
    new_board = []
    for i in range(n+2): # board에 패딩
        if i == 0 or i == n+1: new_board.append([1 for _ in range(n+2)])
        else:
            new_board.append([1]+board[i-1]+[1])
    v = [[0 for _ in range(n+2)] for _ in range(n+2)] # 방문 체크
    v[1][1] = 1
    queue = deque([[1,1,0,-1]])
    dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1];
    while queue:
        x, y, cost, direc = queue.popleft()
        if x == n and y == n: # 도착
            if cost < answer: answer = cost
            continue
        for i in range(4):
            if new_board[x+dx[i]][y+dy[i]] == 0:
                if (direc == -1 or direc == i) and (v[x+dx[i]][y+dy[i]] == 0 or v[x+dx[i]][y+dy[i]] >= cost-300): # 직선 도로
                    queue.append([x+dx[i], y+dy[i], cost+100, i])
                    v[x+dx[i]][y+dy[i]] = cost+100
                elif (direc != -1 and direc != i) and (v[x+dx[i]][y+dy[i]] == 0 or v[x+dx[i]][y+dy[i]] >= cost+200): # 코너
                    queue.append([x+dx[i], y+dy[i], cost+600, i])
                    v[x+dx[i]][y+dy[i]] = cost+600
                
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]), 900)
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]), 3800)
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]), 2100)
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]), 3200)
# tc 24번 다른 방향에서 코너를 들어와 한 칸에서 만났을 때, 다음 값에서 값의 크기가 역전되는 케이스
print(solution([[0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,0],[1,0,0,1,0,0,0,0],[1,1,0,0,0,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0]]), 4500)