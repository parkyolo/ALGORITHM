def solution(arrows):
    answer = 0
    vv = set() # 방문한 점
    ve = set() # 방문한 선

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    cx, cy = 0, 0
    vv.add((cx, cy))

    for arrow in arrows:
        nx = cx+dx[arrow]
        ny = cy+dy[arrow]
        if (cx, cy, nx, ny) in ve or (nx, ny, cx, cy) in ve: # 이미 방문한 선일 때
            cx, cy = nx, ny
            continue
        if (nx, ny) in vv: # 방문한 점과 다시 만날 때
            answer += 1
        if (cx, ny, nx, cy) in ve or (nx, cy, cx, ny) in ve: # 대각선으로 만날 때
            answer += 1
            
        vv.add((nx, ny))
        ve.add((cx, cy, nx, ny))
        cx, cy = nx, ny
            
    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]), 3)
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]), 3)
print(solution([5, 2, 7, 1, 6, 3]), 3)
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]), 3)
print(solution([6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5]), 3)