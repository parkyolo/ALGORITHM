from collections import deque
from copy import deepcopy

def solution(n, info):
    answer = []
    max_score = 0
    queue = deque()
    queue.append([0,0,0,0,[0]*11])
    while queue:
        ascore, lscore, cnt, idx, lion = queue.popleft() # 어피치 score, 라이언 score, 화살을 쏜 횟수, 배열 index, 라이언 기록
        if cnt > n: continue
        if idx > 10:
            if lscore - ascore > max_score:
                max_score = lscore - ascore
                lion[10] = n-cnt
                answer = lion
            else: continue
        new_lion1 = deepcopy(lion)
        new_lion1[10-idx] = info[10-idx]+1
        queue.append([ascore, lscore+idx, cnt+info[10-idx]+1, idx+1, new_lion1]) # 라이언이 점수를 가져갈 때
        new_lion2 = deepcopy(lion)
        if info[10-idx] > 0: queue.append([ascore+idx, lscore, cnt, idx+1, new_lion2]) # 어피치가 점수를 가져갈 때
        else: queue.append([ascore, lscore, cnt, idx+1, new_lion2])
    return answer if answer else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]), [0,2,2,0,1,0,0,0,0,0,0])
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]), [-1])
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]), [1,1,2,0,1,2,2,0,0,0,0])
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]), [1,1,1,1,1,1,1,1,0,0,2])