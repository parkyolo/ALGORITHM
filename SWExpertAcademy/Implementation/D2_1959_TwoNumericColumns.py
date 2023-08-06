'''
1959. 두 개의 숫자열
(https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=%EC%88%AB%EC%9E%90%EB%B0%B0%EC%97%BB&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&)

긴 배열의 길이를 m, 짧은 배열의 길을 n이라고 정하고
긴 배열의 시작 인덱스를 0부터 m-n까지 이동하며 숫자를 곱한다.
'''

t = int(input())

def getMax(n, m, ai, bj):
    answer = 0
    
    for i in range(m-n+1):
        result = 0
        for j in range(n):
            result += ai[j] * bj[i+j]
        answer = max(answer, result)
    
    return answer
        
    
for test_case in range(t):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    answer = 0
    if n > m:
        answer = getMax(m, n, bj, ai)
    else:
        answer = getMax(n, m, ai, bj)
    
    print("#%d %d"%(test_case+1, answer))