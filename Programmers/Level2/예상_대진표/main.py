import math

def solution(n,a,b):
    answer = 1

    while True:
        if a%2 == 0 and a-b == 1:
            break
        elif b%2 == 0 and b-a == 1:
            break
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1

    return answer

print(solution(8, 4, 7), 3)