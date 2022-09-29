dice = list(map(int, input().split()))
horse = [0, 0, 0, 0]
max_score = 0

idx2val = [i*2 for i in range(33)] # idx2val[i] : i번째 칸에 멈췄을 때 얻는 점수
next_idx = [i+1 for i in range(33)] # next_idx[i] : i번째 칸의 다음 칸

idx2val[21] = 0
idx2val[22], idx2val[23], idx2val[24] = 13, 16, 19
idx2val[25], idx2val[26] = 22, 24
idx2val[27], idx2val[28], idx2val[29] = 28, 27, 26
idx2val[30], idx2val[31], idx2val[32] = 25, 30, 35

next_idx[21] = 21
next_idx[5], next_idx[10], next_idx[15] = 22, 25, 27
next_idx[24], next_idx[26] = 30, 30
next_idx[32] = 20

def move(idx, pip):
    dest_idx = horse[idx]
    
    if dest_idx in [5, 10, 15]: # 파란 동그라미 안에서 시작
        dest_idx = next_idx[dest_idx]
        pip -= 1
    
    if dest_idx+pip <= 21:
        dest_idx += pip
    else: # 도착 칸을 넘어가는 범위이거나 안쪽 동그라미를 이동할 때
        for _ in range(pip):
            dest_idx = next_idx[dest_idx]

    if dest_idx == 21: # 도착
        return 21, 0, True

    if dest_idx in horse: # 다른 말이 있을 때
        return horse[idx], 0, False

    return dest_idx, idx2val[dest_idx], True # 이동을 마친 위치, 얻는 점수, 이동 가능 여부

def game(k, sum_score):
    global max_score
    if k == 10: # 모든 주사위를 던짐
        max_score = max(max_score, sum_score)
        return

    for i in range(4):
        if horse[i] == 21: continue # 도착 칸에 있는 말이면 넘어감
        loc, score, canMove = move(i, dice[k]) # 이동을 마친 위치, 얻는 점수, 이동 가능 여부
        if canMove: # 해당 위치로 갈 수 있으면
            temp, horse[i] = horse[i], loc
            game(k+1, sum_score+score)
            horse[i] = temp

game(0, 0)
print(max_score)