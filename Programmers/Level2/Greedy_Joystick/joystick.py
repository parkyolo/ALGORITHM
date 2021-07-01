def solution(name):
    answer = 0
    
    # --> 기존 코드
    # move = []
    # alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # for alpha in name:
    #     move.append(alpha)
    
    # for j in range(len(move)):
    #     index = 0
    #     for i in range(len(alphabet)):
    #         if move[j] == alphabet[i]:
    #             index = i
    #             break
    #     if index > 13:
    #         move[j] = 25-index+1
    #         answer += 25-index+1
    #     else :
    #         move[j] = index
    #         answer += index

    # --> 수정한 코드
    # 상하 조작 횟수를 구함
    move = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    answer = sum(n for n in move)

    # 좌우 조작 횟수를 구함
    idx = 0
    move[0] = 0
    while True:
        left = 0
        right = 0

        # 좌우 이동방향을 정함
        for i in range(idx+1, len(move)):
            if move[i] == 0:
                right += 1
            else:
                right += 1
                break
        for i in range(idx-1, idx-len(move), -1):
            if move[i] == 0:
                left += 1
            else:
                left += 1
                break

        if right > left:
            idx = idx-left
            move[idx] = 0
            answer += left
        else:
            idx = idx+right
            move[idx] = 0
            answer += right

        # --> 기존 코드
        # c = True
        # for n in move:
        #     if n != 0:
        #         c  = False
        # if c == True:
        #     return answer

        # --> 수정한 코드
        if sum(move) == 0:
            return answer

answer = solution('JAN')
print(answer) # 23