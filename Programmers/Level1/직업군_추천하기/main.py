def solution(table, languages, preference):
    answer = [0,'']
    score_table = []
    for t in table:
        score_table.append(t.split())

    for scores in score_table:
        score = 0
        job = scores[0]
        for idx,lang in enumerate(languages):
            if lang in scores: # 각 직업의 직업군 언어 점수가 있다면
                score += preference[idx] * (6 - scores.index(lang)) # 선호도가 곱해서 점수에 더해줌
        if score > answer[0]:
            answer = [score, job]
        elif score == answer[0]: # 점수 총합이 같으면 사전 순으로 먼저 오는 직업을 선택
            if job < answer[1]:
                answer = [score, job]
            
    return answer[1]

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"],[7, 5, 5]),"HARDWARE")
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["JAVA", "JAVASCRIPT"],[7, 5]),"PORTAL")