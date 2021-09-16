start, end = map(int,input().split())
answer = 0

i = 1
num = 1 # 수열의 값
check = True
while check:
    for _ in range(num):
        if i > end: 
            check = False
            break
        # i가 start와 end 사이일 때 answer에 num을 더해줌
        if i >= start: answer += num
        i += 1
    num += 1

print(answer)