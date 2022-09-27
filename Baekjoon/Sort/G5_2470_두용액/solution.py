# 투 포인터를 이용해 두 원소의 합의 절댓값의 최솟값을 구하는 함수
def twoPointer(value, n):
    left, right = 0, n-1                    # 0. 양 끝 포인터 설정, 초기화
    min_value = abs(value[0]+value[1])
    result = [value[0], value[1]]

    while left < right:                     # 두 포인터가 서로 다른 원소를 가리키는 동안 탐색
        sumval = value[left]+value[right]   # 원소의 합
        if sumval == 0:                     # 합이 0이 되면 종료
            return [value[left], value[right]]
        
        if abs(sumval) < min_value:         # 최솟값 갱신
            min_value = abs(sumval)
            result = [value[left], value[right]]
        
        if sumval < 0:                      # 합이 음수이면 더 큰 값 탐색
            left += 1
        else: right -= 1                    # 합이 양수이면 더 작은 값 탐색

    return result

def main():
    N = int(input())
    value = list(map(int, input().split()))
    value.sort()

    answer = twoPointer(value, N)
    print(answer[0], answer[1])

if __name__ == "__main__":
    main()