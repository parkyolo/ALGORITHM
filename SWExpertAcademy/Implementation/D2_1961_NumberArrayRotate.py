'''
1961. 숫자 배열 회전
(https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=%EC%88%AB%EC%9E%90+%EB%B0%B0%EC%97%B4+%ED%9A%8C%EC%A0%84&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

회전했을 때의 index에 있는 숫자를 출력한다.
'''
t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    matrix = list(list(map(int, input().split())) for _ in range(n))
    print('#%d '%test_case)
    for x in range(n):
        for y in range(n):
            print(matrix[n-y-1][x], end='')
        print(' ', end = '')
        for y in range(n):
            print(matrix[n-x-1][n-y-1], end='')
        print(' ', end = '')
        for y in range(n):
            print(matrix[y][n-x-1], end='')
        print()