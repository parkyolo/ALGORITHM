def solution(rows, columns, queries):
    answer = []

    num = 1
    matrix = []
    # rows * columns matrix에 1부터 값을 채움
    for i in range(rows):
        sub_matrix = []
        for j in range(columns):
            sub_matrix.append(num)
            num += 1
        matrix.append(sub_matrix)

    for turn in queries:
        # 시작 인덱스
        start_i = turn[0]-1
        start_j = turn[1]-1
        # 끝 인덱스
        end_i = turn[2]-1
        end_j = turn[3]-1

        temp = matrix[start_i][start_j]
        min_v = temp
        
        # 숫자를 오른쪽으로 돌림
        for i in range(turn[1], turn[3]):
            now = matrix[start_i][i]
            matrix[start_i][i] = temp
            temp = now
            if temp < min_v:
                min_v = temp
        # 숫자를 아래로 돌림
        for i in range(turn[0], turn[2]):
            now = matrix[i][end_j]
            matrix[i][end_j] = temp
            temp = now
            if temp < min_v:
                min_v = temp
        # 숫자를 왼쪽으로 돌림
        for i in range(turn[3]-2, turn[1]-2, -1):
            now = matrix[end_i][i]
            matrix[end_i][i] = temp
            temp = now
            if temp < min_v:
                min_v = temp
        # 숫자를 위로 돌림
        for i in range(turn[2]-2, turn[0]-2, -1):
            now = matrix[i][start_j]
            matrix[i][start_j] = temp
            temp = now
            if temp < min_v:
                min_v = temp
        # 가장 작은 값을 answer에 저장
        answer.append(min_v)        

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]), [8, 10, 25])
# print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]), [1, 1, 5, 3])
# print(solution(100, 97, [[1,1,100,97]]), [1])