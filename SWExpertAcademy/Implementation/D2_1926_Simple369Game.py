'''
1926. 간단한 369게임
(https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1)

'''

n = int(input())

for num in range(1, n+1):
    str_num = str(num)
    instead = "" # 3, 6, 9를 대신할 -
    for sub_str in str_num:
        if sub_str == "3" or sub_str == "6" or sub_str == "9":
            instead += "-"

    if instead: # 3, 6, 9를 포함한 숫자일 때
        print(instead, end="")
    else:
        print(str_num, end="")
 
    print(" ", end="")