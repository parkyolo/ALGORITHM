'''
4008. [모의 SW 역량테스트] 숫자 만들기
(https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH&categoryId=AWIeRZV6kBUDFAVH&categoryType=CODE&problemTitle=4008&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

- 재귀로 순열 함수 구현
- 연산자의 횟수를 빼고 dfs를 호출한 후 dfs가 끝나면 횟수를 다시 더해줌

'''

def cal(a, b, oper): # 연산
    if oper == 0:
        return a+b
    if oper == 1:
        return a-b
    if oper == 2:
        return a*b
    if oper == 3:
        return int(a/b)

def dfs(val, n): # 순열
    global min_val, max_val
    
    if n == N-1:
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        return

    for i in range(4):
        if operators_cnt[i]:
            operators_cnt[i] -= 1
            dfs(cal(val, operands[n+1], i), n+1)
            operators_cnt[i] += 1

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    operators_cnt = list(map(int, input().strip().split()))
    operands = list(map(int, input().strip().split()))

    min_val = 2147483648
    max_val = -2147483648

    dfs(operands[0], 0)
    
    print("#"+str(test_case)+" "+str(max_val-min_val))