def solution(survey, choices):
    answer = ''
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for s, c in zip(survey, choices):
        if 1 <= c <= 3:
            score[s[0]] += 3-c+1
        else:
            score[s[1]] += c-4
    
    indic = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    for a, b in indic:
        if score[a] >= score[b]: answer += a
        else: answer += b
        
    return answer