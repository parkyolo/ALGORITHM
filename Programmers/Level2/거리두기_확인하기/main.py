def solution(places):
    answer = []
    
    for p in places:
        check = True
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    if j+1 < 5:
                        # 오른쪽 1칸
                        if p[i][j+1] == 'P':
                            check = False
                            break
                        # 오른쪽 2칸
                        elif j+2 < 5:
                            if p[i][j+1] == 'O' and p[i][j+2] == 'P':
                                check = False
                                break
                        # 대각선 오른쪽
                        if i+1 < 5:
                            if (p[i][j+1] == 'O' or p[i+1][j] == 'O') and p[i+1][j+1] == 'P':
                                check = False
                                break
                    if i+1 < 5:
                        # 아래 1칸
                        if p[i+1][j] == 'P':
                            check = False
                            break
                        # 아래 2칸
                        elif i+2 < 5:
                            if p[i+1][j] == 'O' and p[i+2][j] == 'P':
                                check = False
                                break
                        # 대각선 왼쪽
                        if j-1 >= 0:
                            if (p[i][j-1] == 'O' or p[i+1][j] == 'O') and p[i+1][j-1] == 'P':
                                check = False
                                break
        if check == True:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
                ["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]), 
                [1, 0, 1, 1, 1, 0])