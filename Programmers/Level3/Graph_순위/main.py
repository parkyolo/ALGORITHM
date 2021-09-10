from collections import deque

def solution(n, results):
    answer = 0
    order = [[0 for _ in range(n)] for _ in range(n)]

    # order[i,j] == 1이면, 선수 i가 선수 j를 이겼다는 의미
    for r in results:
        order[r[0]-1][r[1]-1] = 1

    for i in range(n):
        v = set()
        queue = deque()
        # 선수 i에게 진 선수 j를 queue와 v에 넣음
        for j in range(n):
            if order[i][j] == 1:
                queue.append(j)
                v.add(j)
        # 선수 j에게 진 선수 k는 선수 i에게 진 것과도 같으므로 queue와 v에 넣음
        while queue:
            j = queue.popleft()
            for k in range(n):
                if order[j][k] == 1:
                    if k not in v: 
                        v.add(k)
                        queue.append(k)
        # 선수 i를 이기는 선수 j를 queue와 v에 넣음
        for j in range(n):
            if order[j][i] == 1:
                queue.append(j)
                v.add(j)
        # 선수 j를 이기는 선수 k는 선수 i를 이기는 것과도 같으므로 queue와 v에 넣음
        while queue:
            j = queue.popleft()
            for k in range(n):
                if order[k][j] == 1:
                    if k not in v: 
                        v.add(k)
                        queue.append(k)
        # 선수 i에게 지거나 이기는 선수를 더한 값이 n-1과 같으면 순위가 명확함
        if len(v) == n - 1: answer += 1
        
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]),2)
print(solution(5,[[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]),1)