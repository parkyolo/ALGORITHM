def solution(dirs):
    answer = 0
    
    pi = pj = 5 # 캐릭터의 시작 위치
    visited = [] # 걸어본 길
    
    # 방향이 움직이는 좌표
    direc = ['U', 'D', 'R', 'L']
    di = [-1, 1, 0, 0]
    dj = [0, 0, 1, -1]
    
    for d in dirs:
        index = direc.index(d)
        # 캐릭터가 이동할 좌표
        mi = pi + di[index]
        mj = pj + dj[index]
        
        # 캐릭터가 이동할 좌표가 좌표평면의 경계를 벗어나지 않을 때
        if 0 <= mi <= 10 and 0 <= mj <= 10:
            if d == 'U' or d== 'L':
                # 처음 걸어본 길일 때
                if [mi, mj, pi, pj] not in visited:
                    visited.append([mi, mj, pi, pj])
                    answer += 1
            else:
                if [pi, pj, mi, mj] not in visited:
                    visited.append([pi, pj, mi, mj])
                    answer += 1
            # 캐릭터의 좌표를 이동
            pi = mi
            pj = mj
            
    return answer

print(solution("ULURRDLLU"), 7)
print(solution("LULLLLLLU"), 7)