num = '0123456789abcdefghijklmnopqrstuvwxyz' # 0부터 z까지의 index를 구하기 위한 변수
a, b = input().split()
cnt = 0

def to10(a,i): # 10진수 변환 함수
    lena = len(a)
    result = 0
    for k in range(lena):
        result += i**(lena-k-1) * num.index(a[k])
    return result

result_a = 0
result_b = 0
x = 0
min_a = num.index(max(list(a))) # a의 최소 진법
min_b = num.index(max(list(b))) # b의 최소 진법

for i in range(min_a+1, 37):
    for j in range(min_b+1, 37):
        if i != j: # A != B
            if to10(a,i) == to10(b,j): # 10진법으로 변환한 수가 같으면
                if cnt == 1: # x가 2개 이상일 때
                    print('Multiple')
                    exit(0)
                else:
                    result_a = i
                    result_b = j
                    x = to10(a,i) 
                    cnt = 1
if cnt == 0: print('Impossible') # x가 존재할 수 없을 때
else: # x가 하나만 존재할 때
    print(x, result_a, result_b)