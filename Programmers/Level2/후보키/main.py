from itertools import combinations

def solution(relation):
    answer = 0
    # key index를 배열에 저장
    key_index = [i for i in range(len(relation[0]))]
    combi = [] 
    for i in range(1, len(relation[0])+1):
        # key의 가능한 모든 조합 생성
        temp = combinations(key_index, i) 
        combi += temp

    while combi:
        key = combi.pop(0)

        overlap = [] # 키의 중복을 확인하기 위한 배열
        check = True

        for r in relation:
            # temp에 현재 key의 값을 넣음
            temp = []
            for k in key:
                temp.append(r[k])

            # 중복이 있는지 검사
            if temp in overlap:
                check = False
            else:
                overlap.append(temp)

        # 중복이 없으면 후보키로 사용 가능
        if check == True:
            answer += 1

            length = len(combi) # 현재 combi 배열의 길이를 저장
            iter = 0 # 반복횟수 저장
            index = 0 # key의 인덱스

            while iter < length:
                t = combi[index]
                cnt = 0

                # 최소성을 위해 후보키가 포함된 key는 삭제
                for j in t:
                    for c in key:
                        if c == j:
                            cnt += 1
                if cnt == len(key):
                    del combi[index]
                else:
                    index += 1
                iter += 1
    
    return answer

print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]), 2)