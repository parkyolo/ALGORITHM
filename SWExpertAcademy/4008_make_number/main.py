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