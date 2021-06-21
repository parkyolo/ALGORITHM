def solution(brown, yellow):
    answer = []
    
    # (w-2)*(h-2) = yellow
    # w*h = yellow + brown
    # --> w**2 + (-brown/2-2)*w + (yellow_brown)
    # find solution of the above quadratic equation
    
    b = -brown/2 - 2
    c = yellow + brown
    
    w = (-b + (b**2 -4*c)**0.5) / 2
    h = (-b - (b**2 -4*c)**0.5) / 2
    
    answer.append(w)
    answer.append(h)
    return answer

answer = solution(10, 2)
print(answer) # [4, 3]