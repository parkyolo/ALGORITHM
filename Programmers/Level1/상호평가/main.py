from collections import Counter

def solution(scores):
    answer = ''
    
    for i in range(len(scores)):
        score = list(zip(*scores))[i]
        if max(score) == score[i] or min(score) == score[i]:
            if Counter(score)[score[i]] == 1:
                # 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면
                # 그 점수는 제외하고 평균을 구함
                grade = (sum(score) - score[i])/(len(score)-1)
            else:
                grade = sum(score)/len(score)
        else:
            grade = sum(score)/len(score)
        if grade >= 90: answer += 'A'
        elif grade >= 80: answer += 'B'
        elif grade >= 70: answer += 'C'
        elif grade >= 50: answer += 'D'
        else: answer += 'F'

    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]),"FBABD")
print(solution([[50,90],[50,87]]),"DA")
print(solution([[70,49,90],[68,50,38],[73,31,100]]),"CFD")