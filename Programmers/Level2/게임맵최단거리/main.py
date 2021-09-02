from collections import deque

def solution(maps):

    # 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    player = deque([(0,0)])

    while player:
        i,j = player.popleft()
        for k in range(4):
            # 갈 수 있는 길이고
            if 0 <= i+di[k] < len(maps) and 0 <= j+dj[k] < len(maps[0]):
                # 아직 지나가지 않은 길일 때
                if maps[i+di[k]][j+dj[k]] == 1:
                    # 이전 값을 더해주고 새로운 위치를 저장
                    maps[i+di[k]][j+dj[k]] += maps[i][j]
                    player.append((i+di[k],j+dj[k]))
    
    # 상대 팀 진영에 도착할 수 없을 때
    if maps[-1][-1] == 1: return -1
    # 도착할 수 있을 때
    else: return maps[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]),11)
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]),-1)