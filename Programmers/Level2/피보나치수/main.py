def solution(n): 
    a = 0
    b = 1
    for i in range(2, n+1):
        temp = a + b
        a = b
        b = temp
          
    return b%1234567