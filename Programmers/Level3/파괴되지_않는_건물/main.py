def solution(board, skill):
    answer = 0
    n = len(board); m = len(board[0])
    new_board = [[0 for _ in range(m+1)] for _ in range(n+1)]

    toggle = [0, -1, 1]
    for type_, r1, c1, r2, c2, degree in skill:
        new_board[r1][c1] += toggle[type_] * degree
        new_board[r1][c2+1] -= toggle[type_] * degree
        new_board[r2+1][c1] -= toggle[type_] * degree
        new_board[r2+1][c2+1] += toggle[type_] * degree

    for r in range(1, n): # 위에서 아래도 누적합
        for c in range(m):
            new_board[r][c] += new_board[r-1][c]
    for r in range(n):
        for c in range(1, m): # 왼쪽에서 오른쪽으로 누적합
            new_board[r][c] += new_board[r][c-1]
    for r in range(n): # board에 값을 갱신해주기
        for c in range(m):
            board[r][c] += new_board[r][c]
            if board[r][c] > 0: answer += 1 # 내구도가 0보다 큰 건물 count

    return answer

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]), 10)
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]), 6)