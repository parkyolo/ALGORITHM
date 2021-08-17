def solution(board):
    answer = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], min(board[i-1][j], board[i][j-1])) + 1
        
    for row in board:
        if max(row) > answer:
            answer = max(row)

    answer = answer**2

    # 효율성 통과 실패

    # queue = deque()

    # for i in range(len(board)-1):
    #     for j in range(len(board[0])-1):
    #         if board[i][j] == 1:
    #             queue.append([i,j,1])
    
    # if len(queue) > 0:
    #     answer = 1

    # while queue:
    #     si, sj, length = queue.popleft()
    #     check = True
    #     for i in range(si, si+length+1):
    #         if board[i][sj+length] == 0:
    #             check = False
    #             break
    #     if check ==True:
    #         for j in range(sj, length+sj):
    #             if board[si+length][j] == 0:
    #                 check = False
    #                 break          

    #     if check == True:
    #         if si+length+1 < len(board) and sj+length+1 < len(board[0]):
    #             queue.append([si, sj, length+1])
    #         if (length+1)**2 > answer:
    #             answer = (length+1)**2

    # if answer < 1:
    #     for i in range(len(board)):
    #         if board[i][len(board)-1] == 1:
    #             return 1
    #     for j in range(len(board)):
    #         if board[len(board)-1][j] == 1:
    #             return 1

    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]), 9)
print(solution([[0,0,1,1],[1,1,1,1]]), 4)
print(solution([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]), 9)