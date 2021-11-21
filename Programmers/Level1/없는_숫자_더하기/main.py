def solution(numbers):
    answer = 0
    number = [0,1,2,3,4,5,6,7,8,9]
    for n in number:
        if n not in numbers:
            answer += n
    return answer
print(solution([1,2,3,4,6,7,8,0]),14)
print(solution([5,8,4,0,6,7,9]),6)