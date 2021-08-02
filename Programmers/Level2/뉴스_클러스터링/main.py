def solution(str1, str2):
    answer = 0

    # 대문자, 소문자의 차이 무시
    str1 = str1.upper()
    str2 = str2.upper()

    # 다중 집합
    set1 = []
    set2 = []

    for i in range(len(str1)-1):
        # 기타 공백, 숫자, 특수 문자가 들어있는 경우는 다중집합에 넣지 않음
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i+1]) <= 90:
            set1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if 65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i+1]) <= 90:
            set2.append(str2[i]+str2[i+1])

    # 집합이 모두 공집합일 경우에는 자카드 유사도를 1로 정의
    if len(set1) == 0 and len(set2) == 0: return 65536

    inter = 0
    check = []
    
    for i in set1:
        cntA = 0 # 다중집합 A가 갖고 있는 원소 i의 개수 
        cntB = 0 # 다중집합 B가 갖고 있는 원소 i의 개수
        if i not in check:
            for a in set1:
                if i == a:
                    cntA += 1
            for b in set2:
                if i == b:
                    cntB += 1
            if cntA != 0 and cntB != 0:
                # 원소 i가 겹치는 수는 min(cntA, cntB)
                inter += min(cntA, cntB)
                check.append(i)
    
    # 합집합의 크기 = 두 집합의 크기 - 교집합의 크기
    union = len(set1) + len(set2) - inter

    # 자카드 유사도 = n(A n B) / n(A U B)
    jaccard = inter / union

    answer = int(jaccard * 65536)
    return answer

print(solution("FRANCE", "french"), 16384)
print(solution("handshake", "shake hands"), 65536)
print(solution("aa1+aa2", "AAAA12"), 43690)
print(solution("E=M*C^2", "e=m*c^2"), 65536)