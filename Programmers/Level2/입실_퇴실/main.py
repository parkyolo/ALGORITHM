from collections import deque

def solution(enter, leave):
    # n명의 사람이 만난 사람들
    meet = [set() for _ in range(len(enter))]
    # 현재 회의실에 들어와있는 사람들
    room = set()
    e_queue =  deque(enter)
    l_queue = deque(leave)

    while l_queue:
        if l_queue[0] in room: # 회의실에 들어와있는 사람이 나감
            room.remove(l_queue[0])
            l_queue.popleft()
        else:
            e = e_queue.popleft()
            room.add(e) # 회의실에 사람이 들어옴
            for r in room:
                if e != r:
                    # 현재 회의실에 있는 사람들이 서로 만났다는 것을 표시
                    meet[r-1].add(e)
                    meet[e-1].add(r)
    
    answer = []
    # n명의 사람들이 만난 사람의 수를 카운트해서 answer에 넣음
    for m in meet:
        answer.append(len(m))

    return answer

print(solution([1,3,2],[1,2,3]),[0,1,1])
print(solution([1,4,2,3],[2,1,3,4]),[2,2,1,3])
print(solution([3,2,1],[2,1,3]),[1,1,2])
print(solution([3,2,1],[1,3,2]),[2,2,2])
print(solution([1,4,2,3],[2,1,4,3]),[2,2,0,2])