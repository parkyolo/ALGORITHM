import heapq

hex = {str(i):i for i in range(10)}
hex['A'], hex['B'], hex['C'], hex['D'], hex['E'], hex['F'] = 10, 11, 12, 13, 14, 15

def hex2dec(num): # 16진수를 10진수로 변환하는 함수
    return sum([hex[n]*(16**(len(num)-i-1)) for i, n in enumerate(num)])

def solution(): # 비밀번호를 찾는 함수
    n, k = map(int, input().split())
    nums = input()

    checkSet = set() # 중복 검사를 위한 집합
    createdNums = [] # 중복되지 않은 10진수
    for _ in range(n//4):                               # 1. n//4번 회전하면 제자리로 돌아옴
        for idx in range(0, n, n//4):
            num = nums[idx:idx+n//4]    # 한 변의 숫자
            decNum = hex2dec(num)                       # 2. 10진수 변환
            if decNum not in checkSet:                  # 3. 중복 검사
                checkSet.add(decNum)
                heapq.heappush(createdNums, -decNum)    # 4. 중복되지 않은 10진수를 내림차순으로 우선순위 큐에 추가
        nums = nums[-1] + nums[:-1]                     # 5. 시계방향 회전
    
    for _ in range(k-1): heapq.heappop(createdNums)     # 6. k-1번까지 숫자를 pop
    return -heapq.heappop(createdNums)                  # 7. k번으로 큰 숫자를 반환

T = int(input())

for test_case in range(1, T + 1):
    result = solution()
    print("#%d %d"%(test_case, result))