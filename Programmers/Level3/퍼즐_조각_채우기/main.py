from collections import deque

def turn(puzzle): # 퍼즐을 90도 회전
    rotated = []
    for i in range(len(puzzle[0])):
        temp = []
        for j in range(len(puzzle)-1,-1,-1):
            temp.append(puzzle[j][i])
        rotated.append(temp)
    return rotated

def solution(game_board, table):
    answer = 0
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
            if game_board[i][j] == 0 and v_g[i][j] == 0:
                queue.append((i,j))
                piece.append([x,y])
                v_g[i][j] = 1
                while queue:
                    now_i, now_j = queue.popleft()
                    for k in range(3):
                        if 0 <= now_i + di[k] < n and 0 <= now_j + dj[k] < n:
                            if game_board[now_i + di[k]][now_j + dj[k]] == 0 and v_g[now_i + di[k]][now_j + dj[k]] == 0:
                                queue.append((now_i + di[k],now_j + dj[k]))
                                piece.append([now_i + di[k] - i,now_j + dj[k] - j])
                                v_g[now_i + di[k]][now_j + dj[k]] = 1
                blanks.append(piece)
                piece = []
                x = y = 0

    # ------- 빈칸에 맞는 조각 찾기
    for b in blanks:
        max_w = max_h = -1
        min_w = b[0][1]
        min_h = b[0][0]
        for r in b:
            if r[1] < min_w: min_w = r[1]
            elif r[1] > max_w: max_w = r[1]
            if r[0] < min_h: min_h = r[0]
            elif r[0] > max_h: max_h = r[0]
        width = max_w - min_w + 1
        height = max_h - min_h + 1
        blank = [[0 for _ in range(width)] for _ in range(height)]
        # 빈칸의 width*height 크기의 2차원 배열 생성
        for r in b:
            blank[r[0]][r[1]-min_w] = 1
        check = True
        for p_i, p in enumerate(pieces):
            if check == False: break
            if p == [-1]: continue
            length = len(p)
            max_w = max_h = -1
            min_w = p[0][1]
            min_h = p[0][0]
            for r in p:
                if r[1] < min_w: min_w = r[1]
                elif r[1] > max_w: max_w = r[1]
                if r[0] < min_h: min_h = r[0]
                elif r[0] > max_h: max_h = r[0]
            p_width = max_w - min_w + 1
            p_height = max_h - min_h + 1
            # 빈칸과 width*height 혹은 height*width가 같을 때만 확인
            if (p_height == len(blank) and p_width == len(blank[0])) or (p_height == len(blank[0]) and p_width == len(blank)):
                # 조각의 width*height 크기의 2차원 배열 생성
                piece = [[0 for _ in range(p_width)] for _ in range(p_height)]
                for r in p:
                    piece[r[0]][r[1]-min_w] = 1
                # 조각을 회전하면서 빈칸과 일치하는지 확인
                for _ in range(4):
                    piece = turn(piece)
                    if piece == blank:
                        answer += length
                        pieces[p_i] = [-1] # 사용한 조각은 없앰
                        check = False
                        break       
    return answer


print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]),14)
print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]),0)