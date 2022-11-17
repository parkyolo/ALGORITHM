'''
패턴 마디의 길이
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
'''

T = int(input())

for test_case in range(1, T + 1):
    string = input()
    pattern = string[0]
    for i in range(1, len(string)):
        if string[i] == pattern[0] and string[i:i+len(pattern)] == pattern: # 시작점과 길이가 같으면 패턴
            break
        else:
            pattern += string[i]

    print("#%d %d"%(test_case, len(pattern)))    