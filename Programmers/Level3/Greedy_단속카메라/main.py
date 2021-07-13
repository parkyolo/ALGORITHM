from collections import deque

def solution(routes):
    answer = 0
    
    # 진출 지점의 오름차순으로 정렬
    routes.sort(key=lambda x:x[1])
    
    
    queue = deque()
    queue.append(routes[0][1])
    
    while queue:
        out = queue.popleft() # 가장 빨리 진출하는 차량의 진출지점
        for i in range(len(routes)):
            if routes[i][0] <= out: # 진출하는 차량보다 빨리 진입한 차량은 체크
                routes[i][0] = -1
        for i in range(len(routes)):
            if routes[i][0] != -1: # 아직 지나가지 않은 차량은 queue에 넣음
                queue.append(routes[i][1])
                break
        answer += 1

    return answer

solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]) #2