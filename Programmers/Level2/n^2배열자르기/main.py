def solution(n, left, right):
    answer = []
    
    r = [m+1 for m in range(n)] # 한 행을 나타내는 배열 r
    l = (left-1) // n # (left-1)번째 원소의 행
    for i in range(left%n): # l번째 행일 때 l-1번째 열까지 값이 더해짐
        if i < l:
            r[i] += 1*l-i
    for j in range(left%n, l): # left번째 원소부터는 l-1번째 행까지의 연산만 더해줌
        if l >= j:
            r[j] += 1*(l-1)-j

    # 한 행을 지날 때마다 행번호-1번째 원소까지 1이 더해지는 과정
    # left부터 right까지의 원소에 연산을 해주고 answer배열에 값을 append
    for i in range(left, right+1):
        if i % n == 0:
            l += 1
        if i % n < l:
            r[i%n] += 1
        if left <= i <= right:
            answer.append(r[i%n])

    return answer

print(solution(3,2,5),[3,2,2,3])
print(solution(4,7,14),[4,3,3,3,4,4,4,4])