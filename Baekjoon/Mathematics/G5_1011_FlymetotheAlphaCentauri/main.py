t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    dist = y-x
    moved = 0 # 이동한 거리
    cnt = 0 # 이동 횟수
    iter_num = 1 # 반복 횟수
    while moved < dist:
        moved += iter_num
        cnt += 1
        if cnt % 2 == 0: iter_num += 1
    print(cnt)