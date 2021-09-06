from collections import deque

def cantopen(key,lock,n):
    # 자물쇠의 홈이 열쇠의 돌기보다 많으면 자물쇠를 열 수 없음
    key_dolgi = 0
    lock_hom = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0: lock_hom += 1
            if key[i][j] == 0: key_dolgi += 1
    if lock_hom > key_dolgi: return False
    else: return True

def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 열쇠의 돌기와 홈을 전환시켜서 자물쇠와 같게 만듦
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1: key[i][j] = 0
            else: key[i][j] = 1
    
    # 열쇠를 자물쇠와 같은 크기로 만들어줌
    for i in range(n):
        if i < m:
            for j in range(m,n):
                key[i].append(1)
        else:
            key.append([1 for _ in range(n)])

    queue = deque([key])
    while queue:
        k = queue.popleft()
        if lock == k: return True
        if cantopen(k,lock,n) == False: continue
        
        # key 회전
        rotated_key = k[:]
        for _ in range(3):
            temp_key = []
            for i in range(n):
                temp = []
                for j in range(n-1,-1,-1):
                    temp.append(rotated_key[j][i])
                temp_key.append(temp)
            rotated_key = temp_key[:]
            queue.append(rotated_key)
        # key 이동
        move_to_under = [[1 for _ in range(n)]]
        for i in range(n-1):
            move_to_under.append(k[i])
        move_to_up = []
        for i in range(1, n):
            move_to_up.append(k[i])
        move_to_up.append([1 for _ in range(n)])
        move_to_left = []
        for i in range(n):
            temp = [k[i][j] for j in range(1,n)]
            temp.append(1)
            move_to_left.append(temp)
        move_to_right = []
        for i in range(n):
            temp = [1]
            for j in range(n-1):
                temp.append(k[i][j])
            move_to_right.append(temp)

        queue.append(move_to_under)
        queue.append(move_to_up)
        queue.append(move_to_left)
        queue.append(move_to_right)

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]),True)
print(solution([[0,1],[1,0]], [[0,1,0],[1,0,0],[0,0,1]]))