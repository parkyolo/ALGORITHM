n = int(input())
cnt = 0
arr = [n]
while True:
    temp = []
    # arr에 있는 수로 구할 수 있는 다음 수를 temp에 넣음
    for i in arr:
        if i == 1: # 가장 먼저 1이 되었을 때의 cnt가 연산 횟수의 최솟값임
            print(cnt)
            exit(0)
        if i % 3 == 0: temp.append(i//3)
        if i % 2 == 0: temp.append(i//2)
        temp.append(i-1)
    arr = temp
    cnt += 1