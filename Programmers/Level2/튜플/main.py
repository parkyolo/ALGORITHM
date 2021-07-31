def solution(s):
    answer = []
    sets = []

    n = ''
    # 튜플을 표현하는 집합 기호를 sets 배열에 저장
    for i in s:
        if i == "}":
            if n != '':
                li = list(map(int, n.split(",")))
                sets.append(li)
                n = ''
        elif i == "{":
            n = ''
        else:
            n += i

    length = 1
    # s가 표현하는 튜플을 배열에 담음
    while sets:
        for i in range(len(sets)):
            # 원소가 1개인 집합부터 answer 배열에 담음
            if len(sets[i]) == length:
                for j in sets[i]:
                    # 아직 answer에 담기지 않은 원소이면 answer에 append
                    if j not in answer:
                        answer.append(j)
                # answer에 담은 집합은 삭제
                sets = sets[:i] + sets[i+1:]
                length += 1
                break

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"), [2, 1, 3, 4])
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"), [2, 1, 3, 4])
print(solution("{{20,111},{111}}"), [111, 20])
print(solution("{{123}}"), [123])
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"), [3, 2, 4, 1])