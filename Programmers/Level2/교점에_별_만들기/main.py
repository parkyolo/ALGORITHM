def solution(line):
    answer = []

    inter = [] # 직선의 교점
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            line1 = line[i]
            line2 = line[j]
            a, b, e = line1
            c, d, f = line2
            # 교점 구하기
            if a*d - b*c != 0:
                x, y = 0, 0
                if a*d - b*c != 0:
                    if (b*f - e*d) % (a*d - b*c) == 0:
                        x = (b*f - e*d) // (a*d - b*c)
                        if (e*c - a*f) % (a*d - b*c) == 0:
                            y = (e*c - a*f) // (a*d - b*c)
                            inter.append([x,y])
    # 교점의 최대, 최솟값
    list_i = [i[0] for i in inter]
    list_j = [i[1] for i in inter]
    min_i = min(list_i)
    max_i = max(list_i)
    min_j = min(list_j)
    max_j = max(list_j)

    width = max_i - min_i
    height = max_j - min_j
    # 격자판
    result = [["." for _ in range(width+1)] for _ in range(height+1)]
    for i in inter:
        # 교점의 위치를 옮겨줌
        result[max_j - i[1]][i[0] - min_i] = "*"

    for r in result:
        answer.append("".join(r))
        
    return answer

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
solution([[1, -1, 0], [2, -1, 0]])
solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])