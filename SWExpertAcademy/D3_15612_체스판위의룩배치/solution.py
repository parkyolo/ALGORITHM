'''
체스판 위의 룩 배치

https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYOBfxwaAXsDFATW&categoryId=AYOBfxwaAXsDFATW&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
'''

import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    board = list(input() for _ in range(8))
    row = [False for _ in range(8)]
    col = [False for _ in range(8)]

    cnt = 0         # 룩의 개수
    flag = False    # 서로 다른 두 룩이 같은 열에 있거나 같은 행에 있으면 True

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':       # 1. 룩이 놓여진 칸 도착
                cnt += 1
                if row[i] or col[j]:     # 2. 같은 열이나 행에 다른 룩이 있는 경우
                    print("#%d %s"%(test_case, "no"))
                    flag = True
                    break                # 반복문 종료
                else:                    # 3. 없는 경우
                    row[i] = True        # 방문 체크
                    col[j] = True
        if flag: break

    if not flag:        # 같은 행이나 열에 다른 룩이 없는 경우
        if cnt == 8:    # 룩이 8개 놓여져 있어야 모든 조건 만족
            print("#%d %s" % (test_case, "yes"))
        else:
            print("#%d %s" % (test_case, "no"))