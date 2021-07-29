def solution(n):
    answer = ''
    stack = []

    while n > 0:
        # n을 3으로 나눈 나머지를 stack에 넣음
        stack.append(n%3)
        # n이 3의 배수이면 n // 3 에 1을 더 빼서 3의 배수가 아니게 만듦
        if n % 3 == 0:
            n = n // 3 - 1
            continue
        n //= 3
        
    # stack의 원소를 하나씩 빼면서 string으로 변환
    while stack:
        s = stack.pop()
        # n이 3의 배수일 경우 가장 끝자리는 무조건 "4"
        if s == 0:
            answer += "4"
        else:
            answer += str(s)
            
    return answer

print(solution(1), "1")
print(solution(2), "2")
print(solution(3), "4")
print(solution(4), "11")
print(solution(5), "12")
print(solution(6), "14")
print(solution(7), "21")
print(solution(8), "22")
print(solution(9), "24")
print(solution(10), "41")