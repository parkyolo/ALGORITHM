def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1): # 문자열을 1개씩 잘랐을 때부터 len(s)//2개씩 잘랐을 때까지
        compression = '' # 압축된 문자열을 저장할 변수
        idx = i # 문자열을 슬라이싱할 인덱스
        cnt = 1 # 문자열이 반복된 횟수
        sub_s = s[:idx] # 자른 문자열

        while idx <= len(s):

            # 같은 문자열이 반복되는 경우
            if s[idx:idx+i] == sub_s: 
                cnt += 1 # 반복된 횟수 +1
                idx += i # 다음 인덱스 검사
            else: 
                # 같은 문자열이 반복되지 않을 경우
                if cnt == 1: 
                    # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
                    compression += sub_s
                else:
                    compression += str(cnt) + sub_s
                
                if idx + i <= len(s):
                    sub_s = s[idx:idx+i]
                    idx += i
                    cnt = 1
                # i개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여줌
                else:
                    compression += s[idx:]
                    break

        # 문자열 중 가장 짧은 것의 길이를 answer에 저장
        if len(compression) < answer:
            answer = len(compression)

    return answer

print(solution("aabbaccc"), 7)
print(solution("ababcdcdababcdcd"), 9)
print(solution("abcabcdede"), 8)
print(solution("abcabcabcabcdededededede"), 14)
print(solution("xababcdcdababcdcd"), 17)