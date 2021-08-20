def solution(s):
    answer = ''
    
    strs = list(map(int, s.split(" ")))
    strs.sort()
    answer = str(strs[0]) + " " + str(strs[-1])
    return answer

print(solution("1 2 3 4"),"1 4")
print(solution("-1 -2 -3 -4"), "-4 -1")
print(solution("-1 -1"),"-1 -1")