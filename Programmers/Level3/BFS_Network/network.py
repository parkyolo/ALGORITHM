def solution(n, computers):
    answer = 0

    visited = [] # 모든 컴퓨터를 방문했는지 확인할 리스트
    
    for i in range(n):
        if i in visited: continue

        queue = [] # i번째 컴퓨터와 연결된 컴퓨터를 넣을 큐
        visited.append(i)
        queue.append(i)

        # 네트워크 탐색
        while queue:
            computer = queue.pop(0) # 현재 컴퓨터

            if computer not in visited: # 아직 방문한 적 없는 컴퓨터는 visited에 append
                visited.append(computer)
            
            # 연결된 컴퓨터 탐색
            for j in range(n):
                # 연결되어 있지 않거나 이미 방문한 컴퓨터는 넘어감
                if j == i or computers[computer][j] == 0: continue
                if j in visited: continue

                queue.append(j)
                visited.append(j)

        # 하나의 네트워크를 모두 탐색했음
        answer += 1

    return answer

answer = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
print(answer) #1