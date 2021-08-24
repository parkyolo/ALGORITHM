def find_str(msg, dic):
    length = len(msg)
    while True:
        if msg[:length] in dic:
            return msg[:length], length
        else:
            length -= 1

def solution(msg):
    answer = []
    
    # 길이가 1인 모든 단어를 포함하도록 사전을 초기화
    dic = {}
    asc = 65
    for i in range(1, 27):
        dic[chr(asc)] = i
        asc += 1
        
    index = 27
    i = 0
    
    while msg:
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾음
        w, len_w = find_str(msg, dic)
        # w에 해당하는 사전의 색인 번호 출력
        answer.append(dic[w])
        # 입력에서 처리되지 않은 다음 글자 c가 남아있다면
        if len_w < len(msg):
            # w+c를 다음 색인 번호로 사전에 추가
            dic[msg[:len_w+1]] = index
            index += 1
        # 입력에서 w 제거
        msg = msg[len_w:]

    return answer

print(solution("KAKAO"),[11, 1, 27, 15])
print(solution("TOBEORNOTTOBEORTOBEORNOT"),[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
print(solution("ABABABABABABABAB"),[1, 2, 27, 29, 28, 31, 30])