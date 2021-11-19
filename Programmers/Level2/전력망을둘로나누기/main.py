from collections import deque

def solution(n, wires):
    answer = n
    wires.sort(key=lambda x:x[0])
    queue = deque()
    for i, _ in enumerate(wires):
        v = set()
        if i == 0:
            queue.append(wires[1][0])
            v.add(wires[1][0])
        else:
            queue.append(wires[0][0])
            v.add(wires[0][0])
        while queue: # 트리 만들기
            q = queue.pop()
            for j, w in enumerate(wires):
                if j != i: # i번째 간선을 제외하고 트리를 만듦
                    if w[0] == q and w[1] not in v:
                        queue.append(w[1])
                        v.add(w[1])
                    elif w[1] == q and w[0] not in v:
                        queue.append(w[0])
                        v.add(w[0])
        # 연결된 노트와 연결되지 않은 노드 수의 차이를 구해서
        # answer를 최솟값으로 갱신
        if answer > abs(len(v) - n + len(v)):
            answer = abs(len(v) - n + len(v))
            if answer == 0: # answer가 0이면 바로 종료시킴
                return answer
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]), 3)
print(solution(4, [[1,2],[2,3],[3,4]]), 0)
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]), 1)