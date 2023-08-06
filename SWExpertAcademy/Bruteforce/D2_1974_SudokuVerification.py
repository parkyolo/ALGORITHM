'''
1974. 스도쿠 검증
(https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE&problemTitle=%EC%8A%A4%EB%8F%84%EC%BF%A0+%EA%B2%80%EC%A6%9D&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

행과 열에 대해 검증하고, 왼쪽 위부터 3x3 배열의 숫자가 겹치지 않는지 검증한다.
'''

t = int(input())
puzzle = []

def validRow():
    for x in range(9):
        v = set()
        for y in range(9):
            if puzzle[y][x] in v:
                return False
            else:
                v.add(puzzle[y][x])
    return True

def validCol():
    for y in range(9):
        v = set()
        for x in range(9):
            if puzzle[y][x] in v:
                return False
            else:
                v.add(puzzle[y][x])
    return True

def validSquare(y, x):
    v = set()
    for i in range(3):
        for j in range(3):
            if puzzle[y+j][x+i] in v:
                return False
            else:
                v.add(puzzle[y+j][x+i])
    return True

for test_case in range(1, t+1):
    puzzle = list(list(map(int, input().split())) for _ in range(9))
    answer = -1
    if validRow() and validCol():
        for y in range(0, 7, 3):
            if answer == 0: break
            for x in range(0, 7, 3):
                if not validSquare(y, x):
                    answer = 0
                    break
        if answer == -1:
            answer = 1
    else:
        answer = 0
    print("#%d %d"%(test_case, answer))