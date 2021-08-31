def solution(word):
    answer = 0
    order = {'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    
    for i, w in enumerate(word):
        # w가 A일 때는 가장 앞에 오는 단어이기 때문에 answer += 1
        if w == 'A': answer += 1
        else:
            temp = 0
            # w 앞에 오는 단어들을 count
            # 단어가 5개이므로, 각 자리마다 5의 j승 만큼의 경우의 수가 있음
            for j in range(5-i):
                temp += 5**j
            # w 앞에 오는 단어들이기 때문에 order[w]-1만큼 반복됨
            # w의 순서 = 앞에 오는 단어들을 count한 수 + 1
            answer += temp * (order[w] - 1) + 1
    return answer

print(solution("AAAAE"),6)
print(solution("AAAE"),10)
print(solution("I"),1563)
print(solution("EIO"),1189)