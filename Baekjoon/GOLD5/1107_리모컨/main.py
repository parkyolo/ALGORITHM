n = str(input())
m = int(input())
btns = set()
if m > 0:
    btns = set(map(str, input().split()))

if m == 10: # 모든 버튼이 고장난 경우
    print(abs(int(n) - 100))
    exit()
if m == 9 and '0' not in btns: # 0을 제외한 모든 버튼이 고장난 경우
    print(min(1+int(n), abs(int(n) - 100)))
    exit()

up_channel = n # n보다 같거나 큰 채널 중 버튼으로 이동할 수 있는 채널
while True:
    check = True
    for s in up_channel:
        if s in btns:
            check = False
    if check == True:
        break
    else:
        up_channel = str(int(up_channel) + 1)

down_channel = n # n보다 같거나 작은 채널 중 버튼으로 이동할 수 있는 채널
while True:
    check = True
    for s in down_channel:
        if s in btns:
            check = False
    if check == True:
        break
    else:
        down_channel = str(int(down_channel) - 1)
        if int(down_channel) < 0: break

enter = ""
if int(n) - int(down_channel) > int(up_channel) - int(n) or int(down_channel) < 0:
    enter = up_channel
else:
    enter = down_channel

enter_cnt = len(enter) + abs(int(n) - int(enter))
print(min(enter_cnt, abs(int(n) - 100))) # +,-로만 이동하는 거리와, 채널을 누른 후 이동하는 거리 비교