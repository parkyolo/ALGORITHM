def solution(arr):
    answer = 1

    while True:
        arr.sort()
        check = False
        # 2부터 나누어 떨어지는 수가 있으면 나눈 후 answer에 곱함
        for i in range(2, arr[-1]+1):
            for j in range(len(arr)):
                if arr[j] % i == 0:
                    arr[j] //= i
                    check = True
            if check == True: 
                answer *= i
                break
        # 나누어 떨어지는 수가 없으면 break
        if check == False:
            break

    # 서로소가 된 수들을 answer에 곱함
    for a in arr:
        answer *= a
                
    return answer

print(solution([2,6,8,14]),168)
print(solution([1,2,3]),6)
print(solution([2,3,4]), 12)
print(solution([2,7,14]),14)
print(solution([3,4,9,16]),144)