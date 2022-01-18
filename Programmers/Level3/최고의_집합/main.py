def solution(n, s):    
    if s < n: return [-1] # 최고의 집합이 존재하지 않는 경우
    
    quotient = s//n 
    remainder = s%n 
    elements = [quotient for _ in range(n)] 
    index = n-1
    while remainder:
        elements[index] += 1 
        index -= 1
        remainder -= 1 

    return elements