def solution(A,B):
    answer = 0

    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer

print(solution([1, 4, 2],[5, 4, 4]),29)
print(solution([1,2],[3,4]),10)