from collections import deque

def solution(game_board, table):
    answer = -1
    n = len(game_board)
    v_g = [[0]*n for _ in range(n)]
    v_t = [[0]*n for _ in range(n)]
    # 하좌우 좌표
    di = [1,0,0]
    dj = [0,-1,1]
    
    x = y = 0
    pieces = []
    blanks = []
    piece = []
    queue = deque()
    # 퍼즐 조각 찾기
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and v_t[i][j] == 0:
                queue.append((i,j))
                piece.append([x,y])
                v_t[i][j] = 1
                while queue:
                    now_i, now_j = queue.popleft()
                    for k in range(3):
                        if 0 <= now_i + di[k] < n and 0 <= now_j + dj[k] < n:
                            if table[now_i + di[k]][now_j + dj[k]] == 1 and v_t[now_i + di[k]][now_j + dj[k]] == 0:
                                queue.append((now_i + di[k],now_j + dj[k]))
                                piece.append([now_i + di[k] - i,now_j + dj[k] - j])
                                v_t[now_i + di[k]][now_j + dj[k]] = 1
                pieces.append(piece)
                piece = []
                x = y = 0

    # ------- 빈 칸 찾기 -------
    #         if game_board[i][j] == 0 and v_g[i][j] == 0:
    #             queue.append((i,j))
    #             piece.append([x,y])
    #             v_g[i][j] = 1
    #             while queue:
    #                 now_i, now_j = queue.popleft()
    #                 for k in range(3):
    #                     if 0 <= now_i + di[k] < n and 0 <= now_j + dj[k] < n:
    #                         if game_board[now_i + di[k]][now_j + dj[k]] == 0 and v_g[now_i + di[k]][now_j + dj[k]] == 0:
    #                             queue.append((now_i + di[k],now_j + dj[k]))
    #                             piece.append([now_i + di[k] - i,now_j + dj[k] - j])
    #                             v_g[now_i + di[k]][now_j + dj[k]] = 1
    #             blanks.append(piece)
    #             piece = []
    #             x = y = 0

    # ------- 빈칸에 맞는 조각 찾기
    # pieces.sort(key=len)
    # check = True
    # while check:
    #     for p in pieces:
    #         if p in blanks:
    #             index_p = pieces.index(p)
    #             index_b = blanks.index(p)
    #             pieces = pieces[:index_p] + pieces[index_p+1:]
    #             blanks = blanks[:index_b] + blanks[index_b+1:]
    #             break
    #         else:
    #             check = False
                        
    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]),14)
print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]),0)