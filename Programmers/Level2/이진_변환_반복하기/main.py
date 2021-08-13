def solution(s):
    trans_cnt = 0 # 변환 횟수
    zero_cnt = 0 # 제거된 모든 0의 개수

    while s != '1':
        c = 0 # 0을 제거한 s의 길이

        # s의 문자열이 1이면 c += 1
        # s의 문자열이 0이면 zero_cnt += 1
        for a in str(s):
            if a == '1':
                c += 1
            else:
                zero_cnt += 1

        # c를 이진법으로 표현
        s = bin(c)[2:]

        trans_cnt += 1
    
    return [trans_cnt, zero_cnt]

print(solution("110010101001"), [3,8])
print(solution("01110"), [3,3])
print(solution("1111111"), [4,1])