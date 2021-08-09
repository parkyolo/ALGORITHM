from collections import deque

def solution(m, n, board):
    answer = 0
    game = [list(line) for line in board]

    # 2x2 블록의 좌표
    di = [0, 1, 0, 1]
    dj = [0, 0, 1, 1]
    
    check = True
    while check:   
        check = False
        visited = [] # 한 턴동안 방문한 블록
        for i in range(m-1):
            for j in range(n-1):

                # 같은 모양의 블록이 2x2 형태로 붙어있을 경우
                if game[i][j] != -1 and game[i][j] == game[i+1][j] == game[i][j+1] == game[i+1][j+1]:
                    check = True
                    queue = deque()
                    
                    # 4개의 블록을 queue에 넣고
                    # 아직 방문하지 않은 블록일 경우 answer += 1
                    for k in range(4):
                        queue.append([i+di[k],j+dj[k]])
                        if [i+di[k],j+dj[k]] not in visited:
                            visited.append([i+di[k],j+dj[k]])
                            answer += 1
                    
                    # 2x2 모양이 여러 개 있는지 확인
                    while queue:
                        block = queue.popleft()
                        col = block[0]
                        row = block[1]
                        if col+1 < m and row+1 < n and game[col][row] == game[col+1][row] == game[col][row+1] == game[col+1][row+1]:
                            for k in range(1, 4):
                                if [col+di[k],row+dj[k]] not in visited:
                                    queue.append([col+di[k], row+dj[k]])
                                    visited.append([col+di[k], row+dj[k]])
                                    answer += 1
        
        # 블록 지우기
        for v in visited:
            c = v[0]
            r = v[1]
            for l in range(c, 0, -1):
                game[l][r] = game[l-1][r]
                game[l-1][r] = -1                                
    
    return answer

# print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]), 4)
# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]), 14)
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]), 15)
# print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF'] ), 14)
# print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'] ), 15) 
# print(solution(4, 5, ['AAAAA', 'AUUUA', 'AUUAA', 'AAAAA'] ), 14)
# print(solution(2,2,["AA", "AA"]), 4)
# print(solution(2,2, ["AA", "AB"]), 0)
# print(solution(3,2, ["AA", "AA", "AB"]), 4) 
# print(solution(4,2, ["CC", "AA", "AA", "CC"]), 8)
# print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"]), 12)
# print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]), 8)
# print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"]), 8)
# print(solution(5,6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]), 24)
print(solution(6,6, ["AABBEE", "AAAEEE", "VAAEEV", "AABBEE", "AACCEE", "VVCCEE "]), 32)
# print(solution(4,4, ["ABCD", "BACE", "BCDD", "BCDD"]), 8)